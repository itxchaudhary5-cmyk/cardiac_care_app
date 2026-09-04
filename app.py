import streamlit as st
from groq import Groq

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Cardiac Care App",
    page_icon="🫀",
    layout="centered"
)

# -----------------------------
# Groq Client
# -----------------------------
client = Groq(api_key=st.secrets["GROQ_API_KEY"])

# -----------------------------
# Custom UI
# -----------------------------
st.markdown(
    """
    <style>
    .main-title {
        text-align: center;
        font-size: 42px;
        font-weight: bold;
        margin-bottom: 5px;
    }

    .subtitle {
        text-align: center;
        font-size: 18px;
        margin-bottom: 25px;
    }

    .info-box {
        padding: 18px;
        border-radius: 12px;
        border: 1px solid #ddd;
        margin: 10px 0;
    }

    .emergency-box {
        padding: 20px;
        border-radius: 12px;
        border: 2px solid #d9534f;
        margin: 15px 0;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# -----------------------------
# Sidebar Navigation
# -----------------------------
st.sidebar.title("🫀 Cardiac Care")

page = st.sidebar.radio(
    "Navigate",
    [
        "🏠 Home",
        "🤖 AI Assistant",
        "📚 Heart Health Awareness",
        "🩺 Symptom Checker",
        "🚨 Emergency Information"
    ]
)

# -----------------------------
# HOME
# -----------------------------
if page == "🏠 Home":

    st.markdown(
        '<div class="main-title">🫀 Cardiac Care App</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">Heart Health Awareness & Educational Assistant</div>',
        unsafe_allow_html=True
    )

    st.info(
        "⚠️ This app is for educational and awareness purposes only. "
        "It does not replace a qualified healthcare professional."
    )

    st.markdown("## 🌟 Explore the App")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 🤖 AI Assistant")
        st.write(
            "Ask educational questions about the heart, cardiac health, "
            "symptoms, risk factors and prevention."
        )

    with col2:
        st.markdown("### 🩺 Symptom Checker")
        st.write(
            "Review selected symptoms and receive general safety guidance."
        )

    st.markdown("---")

    st.markdown("### 💡 Important")
    st.write(
        "If someone has severe or rapidly worsening symptoms, "
        "do not rely on this app. Seek urgent medical help."
    )


# -----------------------------
# AI ASSISTANT
# -----------------------------
elif page == "🤖 AI Assistant":

    st.title("🤖 AI Heart Health Assistant")

    st.write(
        "Ask a question about heart health, symptoms, risk factors, "
        "prevention, or general cardiac awareness."
    )

    st.warning(
        "⚠️ This assistant provides educational information only. "
        "It cannot diagnose medical conditions or prescribe treatment."
    )

    question = st.text_area(
        "Ask your question:",
        placeholder="Example: What are common symptoms of heart problems?"
    )

    if st.button("Ask AI", use_container_width=True):

        if not question.strip():
            st.warning("Please enter a question first.")

        else:

            # Emergency keyword check
            emergency_words = [
                "severe chest pain",
                "chest pain and difficulty breathing",
                "chest pain and shortness of breath",
                "difficulty breathing",
                "can't breathe",
                "cannot breathe",
                "fainting",
                "passed out",
                "loss of consciousness",
                "severe breathing problem"
            ]

            question_lower = question.lower()

            emergency_detected = any(
                word in question_lower
                for word in emergency_words
            )

            if emergency_detected:

                st.error("🚨 Possible Medical Emergency")

                st.markdown(
                    """
                    **Severe chest pain, serious breathing difficulty, fainting,
                    or similar symptoms can require immediate medical attention.**

                    Please **seek emergency medical help immediately** and do
                    not wait for the AI response or rely on this app.

                    If you are in Pakistan, contact your local emergency
                    medical service or go to the nearest emergency department.
                    """
                )

            else:

                try:

                    with st.spinner("Thinking..."):

                        response = client.chat.completions.create(
                            model="openai/gpt-oss-20b",
                            messages=[
                                {
                                    "role": "system",
                                    "content": """
You are a heart health educational assistant.

Your purpose is to provide general, easy-to-understand educational
information about heart health.

Important rules:

1. Do not diagnose the user.
2. Do not prescribe medicines or treatment.
3. Do not provide medication doses.
4. If the user describes potentially serious or emergency symptoms,
   clearly advise them to seek immediate medical help.
5. For severe chest pain, severe difficulty breathing, fainting,
   loss of consciousness, or rapidly worsening symptoms, tell the
   user not to wait for the AI and to seek emergency medical care.
6. Keep answers clear, calm and educational.
7. Encourage consultation with a qualified healthcare professional
   when appropriate.
"""
                                },
                                {
                                    "role": "user",
                                    "content": question
                                }
                            ]
                        )

                    st.markdown("### 🫀 AI Response")
                    st.write(response.choices[0].message.content)

                except Exception as e:

                    st.error(
                        "Sorry, something went wrong while connecting "
                        "to the AI service."
                    )

                    st.caption(str(e))


# -----------------------------
# HEART HEALTH AWARENESS
# -----------------------------
elif page == "📚 Heart Health Awareness":

    st.title("📚 Heart Health Awareness")

    with st.expander("🫀 What is the Heart?"):
        st.write(
            "The heart is a muscular organ that pumps blood throughout "
            "the body. Blood carries oxygen and nutrients to tissues "
            "and removes waste products."
        )

    with st.expander("❤️ Common Heart Problems"):
        st.write(
            """
            • Coronary artery disease  
            • Heart failure  
            • Heart rhythm problems  
            • Heart valve diseases  
            • Congenital heart conditions
            """
        )

    with st.expander("⚠️ Common Risk Factors"):
        st.write(
            """
            • High blood pressure  
            • High cholesterol  
            • Smoking  
            • Physical inactivity  
            • Unhealthy diet  
            • Diabetes  
            • Family history
            """
        )

    with st.expander("🌱 Heart-Healthy Habits"):
        st.write(
            """
            • Eat a balanced diet  
            • Stay physically active in a healthy way  
            • Avoid smoking and tobacco  
            • Get adequate sleep  
            • Manage stress  
            • Have regular health checkups
            """
        )


# -----------------------------
# SYMPTOM CHECKER
# -----------------------------
elif page == "🩺 Symptom Checker":

    st.title("🩺 Symptom Checker")

    st.warning(
        "⚠️ This checker provides general safety guidance only. "
        "It does not diagnose a medical condition."
    )

    st.write("Select any symptoms you are experiencing:")

    chest_pain = st.checkbox("Chest discomfort or chest pain")
    breathing = st.checkbox("Severe difficulty breathing")
    fainting = st.checkbox("Fainting or loss of consciousness")
    dizziness = st.checkbox("Severe dizziness")
    weakness = st.checkbox("Sudden weakness")
    heartbeat = st.checkbox(
        "Fast, pounding, or irregular heartbeat"
    )

    if st.button("Check Symptoms", use_container_width=True):

        emergency = (
            chest_pain
            or breathing
            or fainting
            or weakness
        )

        warning = (
            dizziness
            or heartbeat
        )

        if emergency:

            st.error("🚨 Seek Immediate Medical Help")

            st.write(
                "Some of the selected symptoms may require urgent "
                "medical assessment. Please seek emergency medical "
                "help immediately, especially if symptoms are severe "
                "or getting worse."
            )

            st.write(
                "Do not rely on this app to determine the cause "
                "of your symptoms."
            )

        elif warning:

            st.warning("⚠️ Medical Evaluation May Be Appropriate")

            st.write(
                "These symptoms can have many possible causes. "
                "If they are new, persistent, severe, or concerning, "
                "talk to a qualified healthcare professional."
            )

        else:

            st.info(
                "ℹ️ No emergency warning was triggered by the "
                "symptoms selected. This does not rule out a health problem."
            )


# -----------------------------
# EMERGENCY INFORMATION
# -----------------------------
elif page == "🚨 Emergency Information":

    st.title("🚨 Emergency Information")

    st.error(
        "If you think you or someone else may be experiencing "
        "a medical emergency, seek emergency medical help immediately."
    )

    st.markdown("### ⚠️ Concerning Symptoms")

    st.write(
        """
        • Severe or concerning chest pain/discomfort  
        • Severe difficulty breathing  
        • Fainting or loss of consciousness  
        • Sudden severe weakness  
        • Rapidly worsening symptoms  
        """
    )

    st.markdown("### 🏥 What Should You Do?")

    st.write(
        """
        Seek immediate medical attention and contact your local
        emergency medical service or go to the nearest emergency
        department.

        Do not wait for this app or an AI assistant to determine
        whether the situation is serious.
        """
    )

    st.warning(
        "This application is an educational awareness tool and "
        "is not a substitute for emergency medical care."
    )

# -----------------------------
# Footer
# -----------------------------
st.markdown("---")

st.caption(
    "🫀 Cardiac Care App | Heart Health Education & Awareness"
)
