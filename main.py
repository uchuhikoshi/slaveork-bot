import os
import logging

from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import BoundFilter

BOT_TOKEN = os.environ['TGB_TOKEN']
CHAT_ID = os.environ['TG_CHAT_ID']

logging.basicConfig(level=logging.INFO)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

class ChatIdFilter(BoundFilter):
    key = 'chat_id'

    def __init__(self, chat_id):
        self.chat_id = int(chat_id)

    def check(self, message: types.Message) -> bool:
        return message.chat.id == self.chat_id

@dp.message_handler(commands=['help'], chat_id=CHAT_ID)
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/help` command.
    """

    await message.reply("Hi!\nI'm slaveork-bot\nPowered by aiogram.")

@dp.message_handler(regexp='(^cat[s]?$|puss)', chat_id=CHAT_ID)
async def cats(message: types.Message):
    await message.reply("You know he's gone forever")

@dp.message_handler(chat_id=CHAT_ID)
async def echo(message: types.Message):
    await message.answer(f"From:\n{message}\n\n{message.text}")

if __name__ == '__main__':
    dp.filters_factory.bind(ChatIdFilter, event_handlers=[dp.message_handlers])
    executor.start_polling(dp, skip_updates=True)
