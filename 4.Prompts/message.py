from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_cohere import ChatCohere
from dotenv import load_dotenv

load_dotenv()

model = ChatCohere(model = "command-a-03-2025")

message = [
    SystemMessage(content="You are a helpful assistant"),
    HumanMessage(content="Tell me about langchain")
]

result = model.invoke(message)
message.append(AIMessage(content=result.content))
print(message)