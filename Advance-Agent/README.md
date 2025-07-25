---
# 🤖 Chainlit + Gemini Greeting Agent

This project is a simple **AI-powered chatbot** built using [Chainlit](https://docs.chainlit.io/) and **Google Gemini (Generative AI)** through OpenAI-compatible APIs. The agent is designed to handle greetings and basic weather queries in a friendly, culturally contextual way.
---

## ✨ Features

- ✅ **Greeting Agent** – Replies to greetings with “Salam from Hafiz Siddiqui”
- ☁️ **Weather Tool Integration** – Returns dummy weather info using a custom `get_weather` function
- 🧠 **Gemini Model (Flash)** – Powered by Google Gemini (`gemini-2.0-flash`) via OpenAI SDK-style API
- 🔐 **GitHub OAuth** – Secure user login using GitHub OAuth with Chainlit
- 💬 **Chat History Management** – Session-based user chat history

---

## 🚀 Demo Agent Behavior

| User Input                      | Bot Response                                                   |
| ------------------------------- | -------------------------------------------------------------- |
| `Hi` / `Hello`                  | Salam from Hafiz Siddiqui                                      |
| `What's the weather in Lahore?` | The weather in Lahore is 22 degrees C                          |
| `Bye`                           | Allah Hafiz from Hafiz Siddiqui                                |
| `Tell me a joke`                | I'm here just for greeting. Contact Hafiz Siddiqui. Thank you. |

---

## 🛠️ Tech Stack

- **Python**
- **Chainlit**
- **Google Generative AI (Gemini)**
- **dotenv** – For managing API keys securely
- **GitHub OAuth** – Chainlit’s built-in OAuth support

---

## 📁 Project Structure

```
├── agents/
│   └── [Custom Agent + Runner logic here]
├── .env
├── main.py
├── README.md
```

---

## 🧪 Setup & Run

1. **Clone the Repo**

   ```bash
   git clone https://github.com/your-username/chainlit-greeting-agent.git
   cd chainlit-greeting-agent
   ```

2. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Create a `.env` File**

   ```env
   GEMINI_API_KEY=your_gemini_api_key_here
   ```

4. **Run the App**

   ```bash
   chainlit run main.py
   ```

---

## 🔑 Environment Variables

| Variable         | Description                  |
| ---------------- | ---------------------------- |
| `GEMINI_API_KEY` | Google Generative AI API key |

---

## 🔒 GitHub OAuth Setup

Chainlit supports GitHub OAuth by default. To enable:

- Register your app on GitHub Developer Settings
- Set redirect URI to:

  ```
  http://localhost:8000/api/auth/callback/github
  ```

- Add the credentials to your Chainlit config or `.env`

---

## 📬 Contact

Built by **Hafiz Siddiqui**
For more info or collaboration, reach out!

---
