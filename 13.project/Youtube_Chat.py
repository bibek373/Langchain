from langchain_cohere import ChatCohere, CohereEmbeddings
from langchain_core.prompts import PromptTemplate
from langchain_community.vectorstores import FAISS
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled
from langchain_core.runnables import RunnableParallel, RunnablePassthrough, RunnableLambda
from langchain_core.output_parsers import StrOutputParser
from langchain_text_splitters import RecursiveCharacterTextSplitter
from dotenv import load_dotenv
import re
from urllib.parse import urlparse, parse_qs
import streamlit as st

load_dotenv()

st.title("🎬 Chat with YouTube")


# Extract the id from links
def extract_youtube_id(url):
    video_id_pattern = r'[a-zA-Z0-9_-]{11}'
    parsed = urlparse(url)

    if 'watch' in parsed.path:
        query_params = parse_qs(parsed.query)
        if 'v' in query_params:
            return query_params['v'][0]

    elif 'youtu.be' in parsed.netloc:
        video_id = parsed.path.strip('/')
        if re.match(video_id_pattern, video_id):
            return video_id

    elif 'embed' in parsed.path:
        match = re.search(f'/embed/({video_id_pattern})', parsed.path)
        if match:
            return match.group(1)

    elif 'shorts' in parsed.path:
        match = re.search(f'/shorts/({video_id_pattern})', parsed.path)
        if match:
            return match.group(1)

    elif 'attribution_link' in parsed.path:
        query_params = parse_qs(parsed.query)
        if 'u' in query_params:
            nested_url = query_params['u'][0]
            nested_params = parse_qs(urlparse(nested_url).query)
            if 'v' in nested_params:
                return nested_params['v'][0]

    match = re.search(f'[?&]v=({video_id_pattern})', url)
    if match:
        return match.group(1)

    return None


youtube_link = st.text_input("Enter the link of YouTube..!!")
query = st.text_input("Enter your query here...!")


if st.button("Search."):
    if query and youtube_link:
        youtube_id = extract_youtube_id(youtube_link)

        try:
            transcript_list = YouTubeTranscriptApi.list_transcripts(youtube_id)
            transcript = transcript_list.find_transcript(['en', 'en-US'])
            transcript_data = transcript.fetch()

            full_transcript = " ".join(chunk["text"] for chunk in transcript_data)
            
            splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
            chunks = splitter.create_documents([full_transcript])

            embedding_model = CohereEmbeddings(model="embed-english-v3.0")
            vectorstore = FAISS.from_documents(chunks, embedding=embedding_model)

            retriever = vectorstore.as_retriever(
                search_type="similarity",
                search_kwargs={"k": 4}
            )

            llm = ChatCohere(model="command-a-03-2025")

            prompt = PromptTemplate(
                template="""
                You are a helpful assistant.
                If context is insufficient, then say "I don't know".

                {context}
                Question: {question}
                """,
                input_variables=["context", "question"]
            )

            parallel_chain = RunnableParallel({
                "context": retriever | RunnableLambda(lambda docs: "\n\n".join(doc.page_content for doc in docs)),
                "question": RunnablePassthrough()
            })

            parser = StrOutputParser()
            main_chain = parallel_chain | prompt | llm | parser

            result = main_chain.invoke(query)
            st.success(f"Answer:\n{result}")

        except Exception as e:
            st.error(f"Error: {type(e).__name__}: {e}")
    else:
        st.error("❌ Please enter both YouTube link and your question.")
