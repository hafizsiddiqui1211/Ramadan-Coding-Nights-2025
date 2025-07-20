import chainlit as cl
import os


@cl.on_message
async def main(message: cl.Message):
    response = f"You said {message.content}"
    await cl.Message(content=response).send()


if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))
    cl.run("app.py", host="0.0.0.0", port=port, headless=True)
