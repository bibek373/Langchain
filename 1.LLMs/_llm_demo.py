from langchain_cohere import ChatCohere
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

llm = ChatCohere(model="command-a-03-2025",)
result = llm.invoke("What is the capital of Nepal?")

print(result.content)