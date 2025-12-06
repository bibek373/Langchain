from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="mistralai/Mistral-7B-Instruct-v0.2",  
    task="text-generation",
)

model = ChatHuggingFace(llm=llm)

# First prompt -> Detailed report
template1 = PromptTemplate(
    template='Write a detailed report on the {topic}.',
    input_variables={'topic'}
)

# Second prompt -> summary
template2 = PromptTemplate(
    template='Write a 5 line summary on the following text. \n  {text}.',
    input_variables={'text'}
)

prompt1 = template1.invoke({'topic': 'Black holes'})

result = model.invoke(prompt1)

prompt2 = template2.invoke({'text': result.content})

response = model.invoke(prompt2)

print(response.content)