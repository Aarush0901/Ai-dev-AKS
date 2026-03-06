import streamlit as st
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model

# Load environment variables
load_dotenv()

# Initialize model
model = init_chat_model("mistral-small-2506")

st.title("AI Chatbot")

# Session state to store messages
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for i, msg in enumerate(st.session_state.messages):
    if i % 2 == 0:
        st.write(f"You: {msg}")
    else:
        st.write(f"Bot: {msg}")

# Input box
prompt = st.text_input("You:")

if st.button("Send"):
    if prompt == "0":
        st.stop()

    # Add user message
    st.session_state.messages.append(prompt)

    # Get response from model
    response = model.invoke(st.session_state.messages)

    # Store bot response
    st.session_state.messages.append(response.content)

    # Display response
    st.write("Bot:", response.content)