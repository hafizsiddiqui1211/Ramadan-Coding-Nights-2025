import os
import chainlit as cl

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))
    cl.run("app.py", host="0.0.0.0", port=port, headless=True)
