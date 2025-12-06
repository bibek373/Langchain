from langchain_cohere import ChatCohere
from dotenv import load_dotenv

load_dotenv()

model = ChatCohere(model = "command-a-03-2025" , temperature=0.2 , max_comletions_tokens=5)

result = model.invoke("What is the fastest speed of ball in cricket history?")

print(result.content)
