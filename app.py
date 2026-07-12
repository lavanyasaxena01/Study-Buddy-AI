import os
from datetime import datetime

import streamlit as st
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = st.secrets.get(
    "GEMINI_API_KEY",
    os.getenv("GEMINI_API_KEY")
)

client = genai.Client(api_key=api_key)

st.set_page_config(
    page_title="AI Learning Buddy",
    page_icon="🎓",
    layout="wide"
)

st.markdown("""
<style>

.main{
    padding-top:1rem;
}

.title{
    text-align:center;
    font-size:45px;
    font-weight:bold;
    color:#4F8BF9;
}

.subtitle{
    text-align:center;
    color:gray;
    margin-bottom:30px;
}

.stButton>button{
    width:100%;
    border-radius:12px;
    height:3em;
    font-size:18px;
}

.response-box{
    background:#f5f5f5;
    padding:20px;
    border-radius:15px;
    border-left:6px solid #4F8BF9;
}

.footer{
    text-align:center;
    color:gray;
    margin-top:40px;
}

</style>
""", unsafe_allow_html=True)

st.markdown("<div class='title'>🎓 AI Learning Buddy</div>", unsafe_allow_html=True)

st.markdown(
"<div class='subtitle'>Learn Anything with Google Gemini AI</div>",
unsafe_allow_html=True)

st.sidebar.title("📚 Navigation")

st.sidebar.success("Choose a learning activity")

activity = st.sidebar.selectbox(
    "Activity",
    [
        "Explain Concept",
        "Real-Life Example",
        "Generate Quiz",
        "Ask Anything"
    ]
)

difficulty = st.sidebar.select_slider(
    "Difficulty",
    [
        "Beginner",
        "Intermediate",
        "Advanced"
    ]
)

st.sidebar.markdown("---")

st.sidebar.info(
"""
Developed using

• Streamlit

• Google Gemini

• Python
"""
)

if "history" not in st.session_state:
    st.session_state.history=[]

topic = st.text_input(
    "📖 Enter your Topic"
)

if st.button("🚀 Generate Response"):

    if topic.strip()=="":

        st.warning("Please enter a topic.")

    else:

        if activity=="Explain Concept":

            prompt=f"""
You are an expert teacher.

Explain {topic} for a {difficulty} learner.

Use headings.

Use bullet points.

End with a short summary.
"""

        elif activity=="Real-Life Example":

            prompt=f"""
Explain {topic} using one real-life example.

Keep it easy to understand.
"""

        elif activity=="Generate Quiz":

            prompt=f"""
Generate 5 MCQs on {topic}.

Each question should have

A)

B)

C)

D)

Mention the correct answer below every question.
"""

        else:

            prompt=topic

        with st.spinner("🤖 Gemini is Thinking..."):

            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt
            )

            answer = response.text

        st.success("Response Generated!")

        st.markdown(
            f"<div class='response-box'>{answer}</div>",
            unsafe_allow_html=True
        )

        st.download_button(
            "📥 Download Response",
            answer,
            file_name="AI_Response.txt"
        )

        st.session_state.history.append(
            {
                "time":datetime.now().strftime("%I:%M %p"),
                "topic":topic,
                "activity":activity
            }
        )

st.markdown("---")

st.subheader("📜 Learning History")

if len(st.session_state.history)==0:

    st.info("No previous learning sessions.")

else:

    for item in reversed(st.session_state.history):

        st.write(
            f"🕒 {item['time']} • {item['topic']} • {item['activity']}"
        )

st.markdown("---")

st.markdown(
"""
<div class='footer'>

Made with ❤️ using Streamlit + Google Gemini

</div>
""",
unsafe_allow_html=True
)
