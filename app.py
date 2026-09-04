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
        "🩺 Symptom Checker",
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
        "Heart Health Awareness, Symptom Checker, "
        "and Emergency Information."
    )


# AI Assistant
elif page == "🤖 AI Assistant":

    st.title("🤖 AI Heart Health Assistant")

    question = st.text_input(
        "Ask a question about heart health:"
    )

    if st.button("Ask AI"):

        if question:

            try:

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

            except Exception:

                st.error(
                    "Sorry, the AI service is temporarily unavailable. "
                    "Please try again later."
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


# Symptom Checker
elif page == "🩺 Symptom Checker":

    st.title("🩺 Heart Symptom Checker")

    st.write(
        "Select the symptoms you are experiencing. "
        "This tool provides general educational guidance "
        "and does not diagnose medical conditions."
    )

    chest_pain = st.checkbox(
        "Chest discomfort or chest pain"
    )

    breathing = st.checkbox(
        "Severe difficulty breathing"
    )

    fainting = st.checkbox(
        "Fainting or loss of consciousness"
    )

    dizziness = st.checkbox(
        "Severe dizziness"
    )

    weakness = st.checkbox(
        "Sudden weakness"
    )

    palpitations = st.checkbox(
        "Fast, pounding, or irregular heartbeat"
    )

    if st.button("Check Symptoms"):

        emergency_symptoms = (
            chest_pain
            or breathing
            or fainting
            or weakness
        )

        if emergency_symptoms:

            st.error(
                "🚨 Some selected symptoms can require urgent medical attention."
            )

            st.write(
                "Please seek immediate medical help, especially if "
                "the symptoms are severe, sudden, or getting worse."
            )

        elif dizziness or palpitations:

            st.warning(
                "⚠️ These symptoms can have many possible causes. "
                "Consider discussing them with a qualified healthcare professional, "
                "especially if they are new, persistent, or worsening."
            )

        else:

            st.info(
                "No urgent warning was triggered by the selected symptoms. "
                "If you are concerned about your health or symptoms continue, "
                "contact a healthcare professional."
            )


# Emergency Information
elif page == "🚨 Emergency Information":

    st.title("🚨 Emergency Information")

    st.subheader("⚠️ When to Seek Emergency Medical Help")

    st.write(
        "Seek immediate emergency medical help if someone develops "
        "severe or sudden symptoms that may indicate a serious medical problem."
    )

    st.warning(
        "🚨 Concerning symptoms can include:"
    )

    st.markdown("""
    - Severe or sudden chest discomfort
    - Severe difficulty breathing
    - Fainting or loss of consciousness
    - Sudden weakness or difficulty speaking
    - Sudden severe dizziness
    - Symptoms that are rapidly getting worse
    """)

    st.error(
        "If you think someone may be experiencing a medical emergency, "
        "contact your local emergency medical service immediately."
    )

    st.info(
        "This page provides general emergency awareness information. "
        "It is not a substitute for professional medical assessment."
    )
