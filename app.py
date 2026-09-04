import streamlit as st
from groq import Groq

st.set_page_config(
    page_title="Cardiac Care App",
    page_icon="🫀"
)

st.title("🫀 Cardiac Care App")

st.write("Welcome to Cardiac Care App")

st.info(
    "This app provides educational information only. "
    "It does not diagnose or replace professional medical care."
)

client = Groq(
    api_key=st.secrets["GROQ_API_KEY"]
)

st.header("🤖 AI Heart Health Assistant")

question = st.text_input(
    "Ask a question about heart health:"
)

if st.button("Ask AI"):

    if question:

        response = client.chat.completions.create(
            model="openai/gpt-oss-20b",
            messages=[
                {
                    "role": "user",
                    "content": question
                }
            ]
        )

        st.write(response.choices[0].message.content)

    else:
        st.warning("Please enter a question.")
