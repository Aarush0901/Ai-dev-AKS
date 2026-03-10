import chromadb
import json
from openai import OpenAI

print("Starting loader...")

client = OpenAI()

chroma_client = chromadb.PersistentClient(path="./vectordb")

print("Chroma DB initialized")

collection = chroma_client.get_or_create_collection(name="testcases")

print("Collection ready")

with open("testcases.json") as f:
    data = json.load(f)

print("JSON loaded")

for i, tc in enumerate(data):

    text = tc["title"] + " " + tc["steps"]

    embedding = client.embeddings.create(
        model="text-embedding-3-small",
        input=text
    )

    collection.add(
        ids=[str(i)],
        embeddings=[embedding.data[0].embedding],
        documents=[text]
    )

print("Vectors inserted successfully")