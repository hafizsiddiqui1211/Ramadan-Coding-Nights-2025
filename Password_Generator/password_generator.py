import streamlit as st
import random as rd
import string


def password_generator(length, use_digits, use_special):
    characters = string.ascii_letters
    if use_digits:
        characters += string.digits  # Add digits in password
    if use_special:
        characters += string.punctuation  # Add special character in password
    return "".join(rd.choice(characters) for _ in range(length))


st.set_page_config(page_title="🔑 Password Generator", layout="centered")
st.title("🔑 Password Generator by Hafiz Siddiqui")

length = st.slider("Select the length of your password",
                   min_value=12, max_value=24, value=18)
use_digits = st.checkbox("Include digits")
use_special = st.checkbox("Include special characters")

if st.button("Generate Password"):
    password = password_generator(length, use_digits, use_special)
    st.write(f"Your generated password is: {password}")
    st.success("🎊 Congratulations you've got your new password!")
