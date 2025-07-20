import streamlit as st
import requests


def get_random_joke():
    """Fetch a Random Joke from the API"""
    try:
        response = requests.get("https://official-joke-api.appspot.com/random_joke")
        if response.status_code == 200:
            joke_data = response.json()
            return f"{joke_data['setup']}\n\n {joke_data['punchline']}"
        else:
            return "Failed to fetch a joke, please try again later"
    except:
        return "An error occured, please try again later"


def main():
    st.set_page_config(
        page_icon="😜", page_title="Random Joke Generator", layout="centered"
    )
    st.title(
        "😉 Random Joke Generator by [Hafiz Siddiqui](https://www.linkedin.com/in/hafiz-siddiqui-018587295)"
    )
    if st.button("Get a Joke"):
        joke = get_random_joke()
        st.success(joke)
    st.divider()
    st.markdown(
        """<div style='text-align:center;'>
                <p>Joke from official joke API</p>
                </div>""",
        unsafe_allow_html=True,
    )


if __name__ == "__main__":
    main()
