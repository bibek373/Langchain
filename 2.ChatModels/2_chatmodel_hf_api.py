from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="mistralai/Mistral-7B-Instruct-v0.2",  # Different model
    task="text-generation",
    max_new_tokens=512,
)

model = ChatHuggingFace(llm=llm)
response = model.invoke("What is Hugging Face?")
print(response.content)