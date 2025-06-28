import streamlit as st
import google.generativeai as genai

# 🛡️ Configure API Key
genai.configure(api_key="AIzaSyAXaGtYZ8V1bLwtp1KeuTEXD35XTmOWf_E")

# 🧠 Load Gemini Model
model = genai.GenerativeModel("gemini-2.5-flash")

# 🎨 Page Setup
st.set_page_config(page_title="🌍 DE's Chatbot", page_icon="🤖")
st.markdown("""
    <style>
    .stApp {
        background-color: #121212;
        color: #e0e0e0;
        font-family: 'Segoe UI', sans-serif;
    }
    h1, h2, h3 {
        color: #03DAC6;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🤖 DE's Chatbot")
st.write("Chat in your preferred language!")

# 🌐 Language Selector
language = st.sidebar.selectbox(
    "Choose a language for the assistant's response:",
    ["English", "Hindi", "Bengali", "Spanish", "French", "German"]
)

# 🧠 Create Chat Session if not exists
if "chat_session" not in st.session_state:
    st.session_state.chat_session = model.start_chat(history=[])

# 💬 Display Chat History
for msg in st.session_state.chat_session.history:
    with st.chat_message("user" if msg.role == "user" else "assistant"):
        st.markdown(msg.parts[0].text)

# 🧾 User Input
user_prompt = st.chat_input("Type your message...")

if user_prompt:
    # Show user message
    with st.chat_message("user", avatar="🧑‍💻"):
        st.markdown(user_prompt)

    # Prepare multilingual prompt
    translated_prompt = f"Please reply in {language}. User says: {user_prompt}"

    # ✨ Spinner animation while waiting
    with st.chat_message("assistant", avatar="🤖"):
        with st.spinner("thinking..."):
            response = st.session_state.chat_session.send_message(translated_prompt)
            st.markdown(response.text)
