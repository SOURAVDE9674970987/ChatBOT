import streamlit as st
import google.generativeai as genai

# 🔐 API key setup (use environment variable or secrets in production)
genai.configure(api_key="AIzaSyAXaGtYZ8V1bLwtp1KeuTEXD35XTmOWf_E")

# 🌟 Load Gemini model
model = genai.GenerativeModel("gemini-2.5-flash")

# 🧠 Initialize chat session
if "chat_session" not in st.session_state:
    st.session_state.chat_session = model.start_chat(history=[])

st.set_page_config(page_title="💬 DE's Chatbot", page_icon="🤖")
st.title("🤖 DE's Chatbot")

# 💬 Show chat history
for msg in st.session_state.chat_session.history:
    with st.chat_message("user" if msg.role == "user" else "assistant"):
        st.markdown(msg.parts[0].text)

# 🧾 Input area
user_prompt = st.chat_input("Type your message...")

# 🚀 Handle user message
if user_prompt:
    # Show user message
    with st.chat_message("user"):
        st.markdown(user_prompt)

    # Show "thinking..." spinner while waiting for response
    with st.spinner("Thinking..."):
        response = st.session_state.chat_session.send_message(user_prompt)

    # Show assistant response
    with st.chat_message("assistant"):
        st.markdown(response.text)
