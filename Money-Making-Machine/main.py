import streamlit as st
import random
import time
import requests

st.set_page_config(page_title="💱 Money Making Machine", layout="centered")
st.title("💳 Money Making Machine by Hafiz Siddiqui")


def generate_money():
    return random.randint(1, 1000)


st.subheader("Instant Cash Generator")
if st.button("Generate Money"):
    st.write("Counting your money...")
    time.sleep(1)
    amount = generate_money()
    st.success(f"🎉 You've made ${amount}")


def fetch_side_hustle():
    try:
        response = requests.get(
            "http://127.0.0.1:8000/side_hustles?apikey=123456789")
        if response.status_code == 200:
            hustles = response.json()
            return hustles["side-hustle"]
    except:
        st.error("⚠️ Failed to fetch hustle ideas. Try again later.")


st.subheader("Side Hustle Ideas")
if st.button("Genrate Hustle"):
    idea = fetch_side_hustle()
    if idea:
        st.success(f"🎊 Here's a great side hustle idea: {idea}")


def fetch_money_quotes():
    try:
        response = requests.get(
            "http://127.0.0.1:8000/money_quotews?apikey=123456789")
        if response.status_code == 200:
            quotes = response.json()
            return quotes["money_quote"]
    except:
        st.error("⚠️ Failed to fetch money quotes. Try again later.")


st.subheader("Motivational Quotes")
if st.button("Generate Quotes"):
    quote = fetch_money_quotes()
    if quote:
        st.success(f"🎊 Here's a great motivational quote: {quote}")
