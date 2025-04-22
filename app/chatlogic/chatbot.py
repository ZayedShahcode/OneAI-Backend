from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
import os
from app.chatlogic.graph import bot
import asyncio
load_dotenv()

api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    raise ValueError("API key for Groq not found!")

config = {"configurable": {"thread_id": "abc123"}}

async def chat(thread_id,query):
    # language = input("Enter the language: ")
    config["configurable"]["thread_id"] = thread_id
    input_messages = [{"role": "user", "content": query}]
    output =  await bot.ainvoke({"messages": input_messages},config)
    return output["messages"][-1].content

if __name__ == "__main__":
    asyncio.run(chat())