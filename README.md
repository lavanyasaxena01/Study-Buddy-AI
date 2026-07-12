# 🎓 AI Learning Buddy

An AI-powered educational web application built using **Streamlit**. The application helps learners understand concepts through simple explanations, real-life examples, quizzes, and interactive AI responses.

---

## 🚀 Features

- 📖 Explain any concept in beginner-friendly language
- 🌍 Generate real-life examples
- 📝 Create 5 multiple-choice quiz questions with answers
- 💬 Ask anything related to your chosen topic
- 📥 Download AI-generated responses
- 📜 View learning history during the session
- 🎨 Clean and responsive Streamlit interface

---

## 🖥️ Demo

**Live App:** 

Example:

```
https://study-buddy-ai-koty7dybq9wctpdzrqroje.streamlit.app/
```

---

## 🛠️ Tech Stack

- **Frontend:** Streamlit
- **AI Model:** Google Gemini 2.5 Flash
- **Programming Language:** Python
- **Environment Management:** Streamlit Secrets / Environment Variables
- **Deployment:** Streamlit Community Cloud

---

## 📂 Project Structure

```
Study-Buddy-AI/
│
├── app.py
├── requirements.txt
├── README.md
├── screenshots/
├── REFLECTION.md
├── PROMPTS.md
└── .gitignore
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/lavanyasaxena01/Study-Buddy-AI.git
```

### 2. Navigate to the Project Folder

```bash
cd Study-Buddy-AI
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Add Your Gemini API Key

Create a `.env` file:

```env
GEMINI_API_KEY=YOUR_API_KEY
```

or configure it using **Streamlit Secrets** when deploying.

### 5. Run the Application

```bash
streamlit run app.py
```

---

## 🤖 How It Works

1. Enter any topic you want to learn.
2. Choose one of the available learning activities:
   - Explain Concept
   - Real-Life Example
   - Generate Quiz
   - Ask Anything
3. The application sends the prompt to Google's Gemini AI model.
4. Gemini generates an intelligent response.
5. The response is displayed instantly in the web application.

---

## 📚 Learning Activities

### 📖 Explain Concept
Provides beginner-friendly explanations using simple language.

### 🌍 Real-Life Example
Generates practical examples to make concepts easier to understand.

### 📝 Generate Quiz
Creates five multiple-choice questions along with their correct answers.

### 💬 Ask Anything
Allows users to ask any custom question related to the selected topic.

---

## 🔒 Security

- API keys are **never hardcoded** into the application.
- Sensitive credentials are stored using:
  - `.env` (local development)
  - **Streamlit Secrets** (cloud deployment)
- `.env` is excluded from version control using `.gitignore`.

---

## 📈 Future Improvements

- AI chat interface with conversation history
- Voice-based learning assistant
- PDF study notes generation
- Personalized learning recommendations
- Quiz scoring and performance tracking
- Dark mode support
- Multi-language learning support

---

## 🎯 Learning Outcomes

This project demonstrates:

- Streamlit Web Development
- Google Gemini AI Integration
- Prompt Engineering
- Environment Variable Management
- AI-Powered Educational Applications
- Cloud Deployment using Streamlit Community Cloud

---

## 👩‍💻 Author

**Lavanya Saxena**

B.Tech – Artificial Intelligence & Data Science

Dr. Akhilesh Das Gupta Institute of Professional Studies (GGSIPU)

### Connect with me

- GitHub: https://github.com/lavanyasaxena01
- LinkedIn: https://www.linkedin.com/in/lavanya-saxena-6b9b96240

---
