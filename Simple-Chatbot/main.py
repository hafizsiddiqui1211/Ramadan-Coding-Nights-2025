import chainlit as ct


@ct.on_message
async def main(message: ct.Message):
    response = f"You said {message.content}"
    await ct.Message(content=response).send()
