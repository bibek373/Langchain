from langchain_cohere import CohereEmbeddings
from dotenv import load_dotenv

load_dotenv()
embedding=CohereEmbeddings(model="embed-v4.0")
documents=[
    "Kathmandu is the capital of Nepal.",
    "Pokhara is a beautiful city in Nepal.",
    "Mount Everest is the highest mountain in the world."
]

result=embedding.embed_documents(documents)
result_32d = result[:32]

print(str(result_32d))
print(f"Dimensions:{len(result_32d)}")