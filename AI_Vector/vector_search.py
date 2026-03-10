import chromadb
from openai import OpenAI

print("Starting vector search...")

client = OpenAI()

chroma_client = chromadb.PersistentClient(path="./vectordb")

collection = chroma_client.get_collection("testcases")

print("Collection loaded")

query = "Create task chain in datasphere"

embedding = client.embeddings.create(
    model="text-embedding-3-small",
    input=query
)

results = collection.query(
    query_embeddings=[embedding.data[0].embedding],
    n_results=2
)

print("\nMost similar test cases:\n")

for doc in results["documents"][0]:
    print(doc)