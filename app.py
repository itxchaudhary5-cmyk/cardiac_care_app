import streamlit as st
from groq import Groq

st.set_page_config(
    page_title="Cardiac Care App",
    page_icon="🫀"
)

client = Groq(
    api_key=st.secrets["GROQ_API_KEY"]
)

# Sidebar Navigation
page = st.sidebar.selectbox(
    "Menu",
    [
        "🏠 Home",
        "🤖 AI Assistant",
        "📚 Heart Health Awareness",
        "🚨 Emergency Information"
    ]
)

# Home Page
if page == "🏠 Home":

    st.title("🫀 Welcome to Cardiac Care App")

    st.subheader(
        "Your Heart Health Information Assistant"
    )

    st.write(
        "Learn about heart health, understand common symptoms, "
        "and get educational information about cardiac care."
    )

    st.info(
        "⚠️ This app provides educational information only. "
        "It does not diagnose diseases or replace professional medical care."
    )

    st.success(
        "Use the sidebar menu to explore the AI Assistant, "
        "Heart Health Awareness, and Emergency Information."
    )


# AI Assistant
elif page == "🤖 AI Assistant":

    st.title("🤖 AI Heart Health Assistant")

    question = st.text_input(
        "Ask a question about heart health:"
    )

    if st.button("Ask AI"):

        if question:

            response = client.chat.completions.create(
                model="openai/gpt-oss-20b",
                messages=[
                    {
                        "role": "system",
                        "content": (
                            "You are a heart health educational assistant. "
                            "Provide clear, simple and safe health information. "
                            "Do not diagnose diseases. "
                            "If symptoms could indicate a medical emergency, "
                            "clearly advise the user to seek immediate medical care."
                        )
                    },
                    {
                        "role": "user",
                        "content": question
                    }
                ]
            )

            st.write(
                response.choices[0].message.content
            )

        else:

            st.warning(
                "Please enter a question."
            )


# Heart Health Awareness
elif page == "📚 Heart Health Awareness":

    st.title("📚 Heart Health Awareness")

    st.write(
        "Learn general information about heart health, "
        "heart diseases, symptoms, risk factors and prevention."
    )


# Emergency Information
elif page == "🚨 Emergency Information":

    st.title("🚨 Emergency Information")

    st.warning(
        "If someone has severe or sudden symptoms, "
        "seek immediate emergency medical help."
    )

    st.write(
        "Examples of concerning symptoms may include "
        "severe chest discomfort, severe difficulty breathing, "
        "fainting, or sudden weakness."
    )
