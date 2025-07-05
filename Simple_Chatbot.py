#importing necessary libraries
import streamlit as st
import time
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

# Page setup
st.set_page_config(page_title="🤖 Gemini Chatbot", page_icon="💬")
st.title("🤖 Gemini Chatbot")

# Initialising model
chat_model = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0.7, google_api_key=GEMINI_API_KEY)

# Initialising chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [SystemMessage(content="You are a helpful assistant.")]

# displaying chat history
for msg in st.session_state.chat_history:
    if isinstance(msg, HumanMessage):
        with st.chat_message("user", avatar="🧑‍💻"):
            st.markdown(msg.content)
    elif isinstance(msg, AIMessage):
        with st.chat_message("assistant", avatar="🤖"):
            st.markdown(msg.content)

# taking user input
user_input = st.chat_input("💬 Ask me anything...")
if user_input:
    # Showing user message
    with st.chat_message("user", avatar="🧑‍💻"):
        st.markdown(user_input)
    st.session_state.chat_history.append(HumanMessage(content=user_input))

    # Generating model's response
    response = chat_model.invoke(st.session_state.chat_history)
    full_response = response.content

    # Displaying Gemini's response
    with st.chat_message("assistant", avatar="🤖"):
        placeholder = st.empty()
        typed_text = ""
        for char in full_response:
            typed_text += char
            placeholder.markdown(typed_text)
            time.sleep(0.02)  # typing speed (adjust as needed)

    # Saving final response to chat history
    st.session_state.chat_history.append(AIMessage(content=full_response))

# Clear chat button
if st.button("🧹 Clear Chat"):
    st.session_state.chat_history = [SystemMessage(content="You are a helpful assistant.")]
    st.rerun()

  
