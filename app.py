import streamlit as st
from groq import Groq

st.set_page_config(
    page_title="Cardiac Care App",
    page_icon="🫀",
    layout="centered"
)

client = Groq(
    api_key=st.secrets["GROQ_API_KEY"]
)

# Sidebar
st.sidebar.title("🫀 Cardiac Care")
st.sidebar.caption("Heart Health Assistant")

page = st.sidebar.selectbox(
    "Navigate",
    [
        "🏠 Home",
        "🤖 AI Assistant",
        "📚 Heart Health Awareness",
        "🩺 Symptom Checker",
        "🚨 Emergency Information"
    ]
)

st.sidebar.markdown("---")
st.sidebar.caption(
    "Educational information only. "
    "Not a substitute for professional medical care."
)

# Home
if page == "🏠 Home":

    st.title("🫀 Cardiac Care App")
    st.subheader("Your Heart Health Information Assistant")

    st.write(
        "Learn about heart health, understand common symptoms, "
        "and explore educational cardiac information."
    )

    st.info(
        "⚠️ This app provides educational information only. "
        "It does not diagnose diseases or replace professional medical care."
    )

    st.markdown("### Explore the App")

    col1, col2 = st.columns(2)

    with col1:
        st.write("🤖 **AI Assistant**")
        st.write("Ask questions about heart health.")

    with col2:
        st.write("🩺 **Symptom Checker**")
        st.write("Review selected symptoms for general guidance.")

    st.markdown("---")

    st.write(
        "Use the menu on the left to explore all available features."
    )


# AI Assistant
elif page == "🤖 AI Assistant":

    st.title("🤖 AI Heart Health Assistant")

    st.write(
        "Ask a question about heart health and receive "
        "general educational information."
    )

    question = st.text_input(
        "Ask your question:",
        placeholder="Example: What are common symptoms of heart problems?"
    )

    if st.button("Ask AI"):

        if question:

            try:

                with st.spinner("Getting information..."):

                    response = client.chat.completions.create(
                        model="openai/gpt-oss-20b",
                        messages=[
                            {
                                "role": "system",
                                "content": (
                                    "You are a heart health educational assistant. "
                                    "Provide clear, simple and safe health information. "
                                    "Do not diagnose diseases or prescribe treatment. "
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

                st.success("AI Response")
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
                "Please enter a question first."
            )


# Heart Health Awareness
elif page == "📚 Heart Health Awareness":

    st.title("📚 Heart Health Awareness")

    st.subheader("❤️ What is the Heart?")

    st.write(
        "The heart is a muscular organ that pumps blood throughout "
        "the body and helps deliver oxygen and nutrients to tissues."
    )

    st.subheader("⚠️ Common Heart Problems")

    st.write(
        "Common heart-related conditions include coronary artery disease, "
        "heart failure, arrhythmias, and heart valve problems."
    )

    st.subheader("🩺 Common Risk Factors")

    st.write(
        "Risk factors can include high blood pressure, high cholesterol, "
        "diabetes, smoking, physical inactivity, and family history."
    )

    st.subheader("🥗 Heart-Healthy Habits")

    st.write(
        "Healthy habits include a balanced diet, regular physical activity, "
        "adequate sleep, avoiding tobacco, and regular health check-ups."
    )

    st.info(
        "This information is for education and awareness only."
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
                "Consider discussing them with a qualified healthcare "
                "professional, especially if they are new, persistent, "
                "or worsening."
            )

        else:

            st.info(
                "No urgent warning was triggered by the selected symptoms. "
                "If you are concerned or symptoms continue, contact a "
                "healthcare professional."
            )


# Emergency Information
elif page == "🚨 Emergency Information":

    st.title("🚨 Emergency Information")

    st.subheader("⚠️ When to Seek Emergency Medical Help")

    st.write(
        "Seek immediate emergency medical help if someone develops "
        "severe or sudden symptoms that may indicate a serious medical problem."
    )

    st.warning("🚨 Concerning symptoms can include:")

    st.markdown("""
    - Severe or sudden chest discomfort
    - Severe difficulty breathing
    - Fainting or loss of consciousness
    - Sudden weakness
    - Difficulty speaking
    - Sudden severe dizziness
    - Symptoms that are rapidly getting worse
    """)

    st.error(
        "If you think someone may be experiencing a medical emergency, "
        "contact your local emergency medical service immediately."
    )

    st.info(
        "This page provides general emergency awareness information "
        "and is not a substitute for professional medical assessment."
    )
