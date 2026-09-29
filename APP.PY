import streamlit as st
from dotenv import load_dotenv
import os
from google import genai

load_dotenv()
api_key=os.getenv("GEMINI_API_KEY")
client=genai.Client(api_key=api_key)
st.set_page_config(
    page_title="Gemini AI Chatbot",
    page_icon="🤖",
    layout="centered"
)
st.title("Gemini AI Chatbot")
st.write("ask gemini anything!")

prompt=st.text_area(
    "Enter your prompt:",
    placeholder="explain artificial intelligence in simple words..."
)
if st.button("generate response"):
    if prompt:
        with st.spinner("gemini is thinking.... "):
            response=client.models.generate_content(
                model="gemini-3.5-flash-lite",
                contents=prompt
            )
        st.success("Response generated!")
        st.write(response.text)
    else:
        st.warning("please enter a prompt.")