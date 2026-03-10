import chromadb
from openai import OpenAI

client = OpenAI()

# connect to vector DB
chroma_client = chromadb.PersistentClient(path="./vectordb")

collection = chroma_client.get_collection("testcases")


def generate_testcase(user_steps):

    # embed user input
    embedding = client.embeddings.create(
        model="text-embedding-3-small",
        input=user_steps
    )

    # search similar cases
    results = collection.query(
        query_embeddings=[embedding.data[0].embedding],
        n_results=2
    )

    similar_cases = results["documents"][0]

    prompt = f"""
You are a QA automation expert.

User steps:
{user_steps}

Similar existing test cases:
{similar_cases}

Generate a clean structured test case with:
- Title
- Preconditions
- Steps
- Expected Result
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content