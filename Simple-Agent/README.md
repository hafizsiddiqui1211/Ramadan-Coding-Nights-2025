---
# Greeting Agent using Gemini API with OpenAI SDK

This project is a simple AI-powered greeting agent built using the OpenAI Agents SDK, but configured to use Google's **Gemini API** (`gemini-2.0-flash`) for responses. The agent is trained to respond to basic greetings like “hi” or “bye” and to politely reject non-greeting queries.
---

## 💡 Features

- Responds with **"Salam from Hafiz Siddiqui"** when user says `hi`.
- Responds with **"Allah Hafiz from Hafiz Siddiqui"** when user says `bye`.
- For all other inputs, replies with:

  > I'm here just for greeting. Contact Hafiz Siddiqui, Thank You.

- Uses **Gemini 2.0 Flash** model with OpenAI SDK compatibility layer.

---

## 🚀 Installation

1. **Clone this repository**

   ```bash
   git clone https://github.com/yourusername/greeting-agent.git
   cd greeting-agent
   ```

2. **Create and activate a virtual environment (optional but recommended)**

   ```bash
   python -m venv venv
   source venv/bin/activate    # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

---

## 🔐 Environment Variables

Create a `.env` file in the project root directory and add your Gemini API key:

```
GEMINI_API_KEY=your_gemini_api_key_here
```

> Note: Make sure the Gemini API key has access to the `generativelanguage.googleapis.com` endpoint.

---

## 🧠 How it works

- The agent is initialized with a set of instructions.
- User input is taken via `input()` function.
- Based on the input, the agent responds according to the defined logic.
- Non-greeting questions are politely declined.

---

## 🖥️ Usage

```bash
python main.py
```

Example interaction:

```
Please Enter your question:
hi
Salam from Hafiz Siddiqui
```

---

## 📦 Dependencies

- `openai` (OpenAI Agents SDK)
- `python-dotenv` (for loading `.env`)
- `asyncio` (used internally by Runner)
- Compatible with Python 3.8+

---

## 📄 File Structure

```
.
├── main.py           # Main script
├── .env              # Your Gemini API key
├── requirements.txt  # Python dependencies
└── README.md         # You're reading it!
```

---

## ✍️ Author

**Hafiz Wildan Ahmed Siddiqui**
_Contact me for help or customization._

---

## 🛑 Disclaimer

This is a basic demo for educational/testing purposes and is not production-ready. Use the Gemini API responsibly and ensure your usage complies with Google’s terms of service.

---
