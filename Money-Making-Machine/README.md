
# 💱 Money Making Machine

A fun and interactive Streamlit app that generates random money, provides side hustle ideas, and displays motivational money-related quotes.

## 🚀 Features
- 💰 **Instant Cash Generator**: Click a button to generate a random amount of money.
- 🔥 **Side Hustle Ideas**: Fetches creative business or side hustle ideas from an API.
- 📜 **Motivational Quotes**: Displays inspiring quotes about money.

## 🛠️ Setup Instructions

### 1️⃣ Install Dependencies
Make sure you have Python installed, then install the required libraries:
```bash
pip install streamlit requests
```

### 2️⃣ Run the App
Execute the following command in your terminal:
```bash
streamlit run app.py
```

### 3️⃣ API Configuration
The app fetches data from a local API running at `http://127.0.0.1:8000`. Ensure the API is running and provides:
- `/side_hustles?apikey=123456789` → Returns side hustle ideas.
- `/money_quotews?apikey=123456789` → Returns money-related quotes.

## 🐞 Known Issues
- If the API is not running, the app will display an error message when fetching hustle ideas or quotes.
- There's a typo in `fetch_money_quotes()` where `"money_quotews"` should be `"money_quotes"`.

## 📌 Author
Developed by **Hafiz Siddiqui**.

## 🔗 License
This project is open-source and free to use.
```
