import os  # For accessing environment variables
import chainlit as cl  # Web UI framework for chat applications
from dotenv import load_dotenv  # For loading environment variables
from typing import Optional, Dict  # Type hints for better code clarity
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel
from agents.tool import function_tool

# Load environment variables from .env file
load_dotenv()

# Get Gemini API key from environment variables
gemini_api_key = os.getenv("GEMINI_API_KEY")

provider = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai",
)
model = OpenAIChatCompletionsModel(model="gemini-2.0-flash", openai_client=provider)


@function_tool("get_weather")
def get_weather(location: str, unit: str = "C") -> str:
    """Fetch the weather for a given location, return the weather"""
    return f"The weather in {location} is 22 degrees {unit}"


agent = Agent(
    name="Greeting Agent",
    instructions="You are a greeting agent, Your task is to greet the user with a friendly message, when someone says hi you've reply back Salam from Hafiz Siddiqui,if someone asks about weather then use the get_weather tool to get the waeter. if someone says bye then say Allah Hafiz from Hafiz Siddiqui, when someone asks other than greeting then say I'm here just for greeting. Contact Hafiz Siddiqui, Thank You",
    model=model,
    tools=[get_weather],
)


# Decorator to handle OAuth callback from GitHub
@cl.oauth_callback
def oauth_callback(
    provider_id: str,  # ID of the OAuth provider (GitHub)
    token: str,  # OAuth access token
    raw_user_data: Dict[str, str],  # User data from GitHub
    default_user: cl.User,  # Default user object from Chainlit
) -> Optional[cl.User]:  # Return User object or None
    """
    Handle the OAuth callback from GitHub
    Return the user object if authentication is successful, None otherwise
    """

    print(f"Provider: {provider_id}")  # Print provider ID for debugging
    print(f"User data: {raw_user_data}")  # Print user data for debugging

    return default_user  # Return the default user object


# Handler for when a new chat session starts
@cl.on_chat_start
async def handle_chat_start():
    cl.user_session.set("history", [])  # Initialize empty chat history

    await cl.Message(
        content="Hello! How can I help you today?"
    ).send()  # Send welcome message


# Handler for incoming chat messages
@cl.on_message
async def handle_message(message: cl.Message):
    history = cl.user_session.get("history")  # Get chat history from session

    history.append(
        {"role": "user", "content": message.content}
    )  # Add user message to history

    result = await cl.make_async(Runner.run_sync)(agent, input=history)
    response_text = result.final_output
    await cl.Message(content=response_text).send()
    history.append({"role": "assistant", "content": response_text})
    cl.user_session.set("History:", history)
