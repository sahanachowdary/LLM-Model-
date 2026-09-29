import streamlit as st
import ollama

st.set_page_config(
    page_title="AI Chatbot",
    page_icon="🤖"
)

st.title("🤖 MY AI CHATBOT")
st.caption("powered by ollama+streamlit")

if "messages" not in st.session_state:
    st.session_state.messages = []
# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Chat input
prompt = st.chat_input("Ask me anything...")
if prompt:
    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    with st.chat_message("user"):
        st.write(prompt)

    # Ollama response
    with st.chat_message("assistant"):
        response = ollama.chat(
            model="llama3.2",
            messages=st.session_state.messages
        )

        reply = response["message"]["content"]
        st.markdown(reply)

    st.session_state.messages.append({
        "role": "assistant",
        "content": reply
    })