import streamlit as st
import google.generativeai as genai
from datetime import datetime

# ----------------------------
# Configure Gemini API
# ----------------------------
from dotenv import load_dotenv
import os

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel("gemini-2.5-flash")

# ----------------------------
# Page Configuration
# ----------------------------
st.set_page_config(
    page_title="AI Learning Buddy",
    page_icon="🎓",
    layout="wide"
)

# ----------------------------
# Sidebar
# ----------------------------
st.sidebar.title("📚 AI Learning Buddy")

st.sidebar.info(
"""
This AI Buddy helps you:

✅ Explain Concepts

✅ Real-life Examples

✅ Generate Quiz

✅ Ask Anything
"""
)

st.sidebar.markdown("---")
st.sidebar.write("Developed using")
st.sidebar.write("• Streamlit")
st.sidebar.write("• Google Gemini")
st.sidebar.write("• Python")

# ----------------------------
# Main Page
# ----------------------------
st.title("🎓 AI Learning Buddy")

st.write(
"Learn any concept quickly with AI-powered explanations, examples and quizzes."
)

# ----------------------------
# Session History
# ----------------------------
if "history" not in st.session_state:
    st.session_state.history = []

topic = st.text_input("📖 Enter Topic")

activity = st.selectbox(
    "Choose Activity",
    [
        "Explain Concept",
        "Real-Life Example",
        "Generate Quiz",
        "Ask Anything"
    ]
)

difficulty = st.select_slider(
    "Difficulty Level",
    ["Beginner","Intermediate","Advanced"]
)

if st.button("🚀 Generate"):

    if topic.strip()=="":

        st.warning("Please enter a topic.")

    else:

        if activity=="Explain Concept":

            prompt=f"""
Explain {topic} for a {difficulty} learner.

Use:
• Simple language
• Bullet points
• Important keywords
• Summary at the end.
"""

        elif activity=="Real-Life Example":

            prompt=f"""
Give a simple real-life example to explain {topic}.
"""

        elif activity=="Generate Quiz":

            prompt=f"""
Create 5 MCQs on {topic}.

Each question should have:
A
B
C
D

Mention correct answer after every question.
"""

        else:

            prompt=topic

        with st.spinner("Generating AI Response..."):

            response=model.generate_content(prompt)

            answer=response.text

            st.success("Generated Successfully!")

            st.markdown(answer)

            st.download_button(
                "📥 Download Response",
                answer,
                file_name="AI_Response.txt"
            )

            st.session_state.history.append(
                {
                    "time":datetime.now().strftime("%H:%M"),
                    "topic":topic,
                    "activity":activity
                }
            )

# ----------------------------
# History
# ----------------------------
st.markdown("---")

st.subheader("📜 Learning History")

if len(st.session_state.history)==0:

    st.write("No activity yet.")

else:

    for item in reversed(st.session_state.history):

        st.write(
            f"🕒 {item['time']} | **{item['topic']}** ({item['activity']})"
        )

# ----------------------------
# Footer
# ----------------------------
st.markdown("---")

st.caption("Made with ❤️ using Streamlit & Google Gemini")