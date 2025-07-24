---
# 🤖 Chainlit + Gemini Chatbot with GitHub OAuth

This project is a **chatbot web app** built using [Chainlit](https://docs.chainlit.io) and **Google's Gemini 2.0 Flash** model. It features GitHub OAuth login and maintains a conversation history using Chainlit's session management.
---

## 🚀 Features

- 🔐 **GitHub OAuth Login** – Authenticates users using GitHub.
- 💬 **Conversational Memory** – Maintains chat history for each session.
- ⚡ **Gemini 2.0 Flash Integration** – Uses Google’s fast and efficient LLM.
- 🌐 **Chainlit UI** – Provides an interactive, real-time chat interface.

---

## 📦 Requirements

- Python 3.9+
- `chainlit`
- `google-generativeai`
- `python-dotenv`

---

## 🛠️ Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/chainlit-gemini-chatbot.git
   cd chainlit-gemini-chatbot
   ```

2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Create a `.env` file with your Gemini API key:**

   ```
   GEMINI_API_KEY=your_api_key_here
   ```

4. **Run the app:**

   ```bash
   chainlit run app.py
   ```

---

## 🧠 How It Works

- On app launch, users are greeted with a welcome message.
- When a user sends a message, it is stored in session history.
- The full history is sent to the Gemini model to generate a context-aware response.
- The response is displayed in the UI and appended to the session.

---

## 🔑 OAuth Callback

This app includes a GitHub OAuth callback handler using Chainlit's built-in `@cl.oauth_callback`. User data is printed for debugging, and a default user object is returned.

---

## 📁 Project Structure

```
├── app.py           # Main Chainlit application
├── .env             # Environment variables (not committed)
└── requirements.txt # Python dependencies
```

---

## 📝 License

This project is open-source and available for use.

---

## 🙋‍♂️ Author

Built with 💙 by [Hafiz Siddiqui](https://x.com/hafiz_siddiqui_)

---
