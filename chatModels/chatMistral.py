from dotenv import load_dotenv
load_dotenv()

from langchain.chat_models import init_chat_model

model = init_chat_model("mistral-small-2506")

response = model.invoke("Write a HINGLISH poem on AI", temperature= 0.9)
#max_tokens=50 this set limit for the output
print(response.content)