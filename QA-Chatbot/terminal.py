import google.generativeai as gemini
from dotenv import load_dotenv
import os

load_dotenv()
gemini.configure(api_key=os.environ["GEMINI_API_KEY"])
model = gemini.GenerativeModel(model_name="gemini-2.0-flash")
while True:
    user_input = input("Enter your query:\n\tOR\nwrite (quit) to exit.\n")
    if user_input.lower() == "quit":
        print("Thanks for chatting, Goodbye!!!")
        break
    else:
        response = model.generate_content(user_input)
        print("\nResponse:\n\t", response.text)
