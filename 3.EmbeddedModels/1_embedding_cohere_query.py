from langchain_cohere import CohereEmbeddings
from dotenv import load_dotenv

load_dotenv()
embedding=CohereEmbeddings(model="embed-v4.0")

result=embedding.embed_query("kathmandu is the capital of Nepal.")
result_32d = result[:32]

print(str(result_32d))
print(f"Dimensions:{len(result_32d)}")