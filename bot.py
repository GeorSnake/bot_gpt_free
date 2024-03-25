import os
import nest_asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command
from g4f.client import Client

# Apply nest_asyncio to allow using blocking functions in an async environment
nest_asyncio.apply()

# Set up the bot token
BOT_TOKEN = 'YOUR_BOT_TOKEN'

# Initialize the bot and dispatcher
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Initialize the g4f client
client = Client()

# Function to send a request to ChatGPT and process the response
def ask(prompt: str) -> str:
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
    )
    # Remove '**' and '#' symbols from the ChatGPT response
    return response.choices[0].message.content.replace('**', '').replace('#', '')

# Handler for the /start command
@dp.message(Command(commands=['start']))
async def send_welcome(message: Message):
    await message.answer("Hi! I'm a bot powered by ChatGPT. Send me a message, and I'll forward it to ChatGPT.")

# Handler for text messages
@dp.message()
async def chatgpt_handler(message: Message):
    # Send the user's message to ChatGPT and get the response
    response = ask(message.text)
    # Send the processed response back to the user
    await message.answer(response)

# Run the bot
if __name__ == '__main__':
    dp.run_polling(bot)