---
# 🤖 Chainlit + Gemini Chatbot

This is a simple **AI chatbot** built using [Chainlit](https://docs.chainlit.io/) and **Google Gemini (Generative AI)**.
The chatbot responds to user messages by generating answers using the `gemini-2.0-flash` model.
---

## ✨ Features

- **Google Gemini Integration** – Leverages Google's generative AI model for intelligent responses.
- **Chainlit UI** – Provides a clean and interactive chat interface.
- **Environment Variables** – Securely loads API keys via `.env`.
- **Async Response Handling** – Smooth and responsive message processing.

---

## 🛠️ Setup & Installation

### 1. Clone the Repository

```bash
git clone <repo-url>
cd <repo-folder>
```

### 2. Create and Activate Virtual Environment

```bash
python -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

(If `requirements.txt` is not available, manually install:)

```bash
pip install chainlit google-generativeai python-dotenv
```

### 4. Set Environment Variables

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_google_gemini_api_key
```

---

## 🚀 Run the Chatbot

```bash
chainlit run main.py
```

Then open the local URL displayed in the terminal (usually `http://localhost:8000`).

---

## 📂 Project Structure

```
.
├── main.py          # Main chatbot logic
├── .env             # Environment variables (not committed)
└── README.md        # Project documentation
```

---

## 📝 How It Works

1. When a user sends a message, Chainlit triggers the `@cl.on_message` event.
2. The message content is passed as a **prompt** to Gemini's `generate_content()` method.
3. Gemini generates a response, which is displayed in the chat UI.

---
