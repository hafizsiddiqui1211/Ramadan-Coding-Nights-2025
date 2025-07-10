import streamlit as st
import random as rd
import time

# 🛠 Page Config
st.set_page_config(
    page_title="Quiz App",
    page_icon="📋",
    layout="centered",
)

# 🧠 Title
st.title(
    "❓ Quiz App by [Hafiz Siddiqui](https://www.linkedin.com/in/hafiz-siddiqui-018587295)"
)

# ✅ Questions List
questions = [
    {
        "question": "What's the capital of Pakistan?",
        "options": ["Karachi", "Lahore", "Islamabad", "Peshawar"],
        "answer": "Islamabad",
    },
    {
        "question": "Who is the founder of Pakistan?",
        "options": ["Allama Iqbal", "M.A.Jinnah", "Liaquat Ali Khan", "Fatima Jinnah"],
        "answer": "M.A.Jinnah",
    },
    {
        "question": "What is the national language of Pakistan?",
        "options": ["Sindhi", "Balochi", "Urdu", "Pashto"],
        "answer": "Urdu",
    },
    {
        "question": "Which city is known as the city of lights in Pakistan?",
        "options": ["Karachi", "Lahore", "Quetta", "Peshawar"],
        "answer": "Karachi",
    },
    {
        "question": "What's the currency of Pakistan?",
        "options": ["PKR", "INR", "SAR", "USD"],
        "answer": "PKR",
    },
]

# 🎲 Choose random question if not already selected
if "current_question" not in st.session_state:
    st.session_state.current_question = rd.choice(questions)

question = st.session_state.current_question

# ❓ Show Question
st.subheader(f"Question: {question['question']}")

# 🧾 Answer Options
selected_option = st.radio("Choose your answer:", question["options"], key="answer")

# 🔘 Button
if st.button("Submit Answer"):
    if selected_option == question["answer"]:
        st.success("✅ Correct Answer!")
        st.balloons()
    else:
        st.error(f"❌ Wrong! Correct answer: {question['answer']}")

    time.sleep(2)
    st.session_state.current_question = rd.choice(questions)
    st.rerun()
