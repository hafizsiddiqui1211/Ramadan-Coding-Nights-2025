# 💬 Simple Echo Bot with Chainlit

This is a minimal **Chainlit application** that echoes back whatever the user sends.
It demonstrates how to create a basic chatbot using [Chainlit](https://docs.chainlit.io).

---

## 🚀 Features

- **Message Echo** – Replies with "You said \<message\>" for every user input.
- **Asynchronous Handling** – Built using async functions for smooth performance.
- **Lightweight & Simple** – A great starting point for any Chainlit-based app.

---

## 📂 Code Overview


import chainlit as ct

@ct.on_message
async def main(message: ct.Message):
    response = f"You said {message.content}"
    await ct.Message(content=response).send()


## 🛠️ Installation & Setup

1. **Create a virtual environment** (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate    # On Windows: venv\Scripts\activate
   ```

2. **Install Chainlit**:

   ```bash
   pip install chainlit
   ```

3. **Run the app**:

   ```bash
   chainlit run app.py
   ```

   (Replace `app.py` with your filename.)

4. **Open in browser**:
   After running, visit [http://localhost:8000](http://localhost:8000).

---

## 📌 Usage

Type any message in the chat, and the bot will reply:

```
User: Hello!
Bot:  You said Hello!
```

---

## 🧑 Author

Developed by **Hafiz Siddiqui**.
For more about Chainlit, see [https://docs.chainlit.io](https://docs.chainlit.io).


