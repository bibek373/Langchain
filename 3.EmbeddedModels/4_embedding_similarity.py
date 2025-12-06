from langchain_cohere import CohereEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()
embedding = CohereEmbeddings(model='embed-v4.0')

doucuments = [
    "Kathmandu is the capital of Nepal.",
    "Pokhara is a beautiful city in Nepal.",
    "Mount Everest is the highest mountain in the world.",
    "Lumbini is the birthplace of Lord Buddha."
]

query = 'lord buddha birthplace' 

doc_embeddings = embedding.embed_documents(doucuments)
query_embedding = embedding.embed_query(query)

score=cosine_similarity([query_embedding], doc_embeddings)[0]

index , score =sorted(list(enumerate(score)),key=lambda x:x[1])[-1]

print(query)
print(doucuments[index])
print("Similarity Score:", score)