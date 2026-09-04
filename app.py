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

    st.subheader("Your Heart Health Information Assistant")

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

    st.subheader("❤️ What is the Heart?")

    st.write(
        "The heart is a muscular organ that pumps blood throughout "
        "the body. It supplies oxygen and nutrients to tissues "
        "and removes waste products."
    )

    st.subheader("⚠️ Common Heart Problems")

    st.write(
        "Some common heart-related conditions include coronary "
        "artery disease, heart failure, arrhythmias, and heart valve problems."
    )

    st.subheader("🩺 Common Risk Factors")

    st.write(
        "Important risk factors can include high blood pressure, "
        "high cholesterol, diabetes, smoking, physical inactivity, "
        "and a family history of heart disease."
    )

    st.subheader("🥗 Heart-Healthy Habits")

    st.write(
        "Healthy habits include eating a balanced diet, staying "
        "physically active, getting adequate sleep, avoiding tobacco, "
        "and having regular health check-ups."
    )

    st.info(
        "This information is for education and awareness only "
        "and should not be used to diagnose or treat a medical condition."
    )


# Emergency Information
elif page == "🚨 Emergency Information":

    st.title("🚨 Emergency Information")

    st.warning(
        "If someone has severe or sudden symptoms, "
        "seek immediate emergency medical help."
    )

    st.write(
        "Examples of concerning symptoms may include severe chest "
        "discomfort, severe difficulty breathing, fainting, or sudden weakness."
    )
