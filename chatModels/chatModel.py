from dotenv import load_dotenv
load_dotenv()

from langchain.chat_models import init_chat_model

model = init_chat_model("mistral-small-2506")

messages=[]

#max_tokens=50 this set limit for the output


while True:
    print("-----------Welcome Type 0 to exit the application-----------")
    prompt= input("You: ")
    messages.append(prompt)
    if prompt=="0":
        break
    response = model.invoke(messages)
    messages.append(response.content)
    print("Bot: ",response.content)
    

print(messages)