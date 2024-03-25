# bot_gpt_free
Telegram bot with ChatGPT integration This project is a Telegram bot that uses the capabilities of the ChatGPT language model to generate responses to users' messages. The bot is based on aiogram library for working with Telegram API and g4f library for interacting with ChatGPT.
## Bot features
- Processing the /start command to send a welcome message to the user.
- Processing user text messages and sending them to ChatGPT to generate a reply.
- Automatically removing special characters(** and #) from ChatGPT responses to improve readability.
- Sending the generated reply back to the user in Telegram chat.

## Installation and customization
1)Clone the repository:
`git clone https://github.com/your_username/chatgpt-telegram-bot.git`

2)Install the necessary dependencies:
`pip install aiogram g4f nest_asyncio`

3)Replace 'YOUR_BOT_TOKEN' with your Telegram bot token obtained from BotFather:
`python bot.py`

:+1: __Теперь ваш бот готов к работе и может обрабатывать сообщения пользователей, используя возможности ChatGPT.__

## Dependencies
- `aiogram` - library for working with Telegram API
- `g4f` - library for interacting with ChatGPT
- `nest_asyncio` - library for using blocking functions in asynchronous environment
