import os
import logging

from aiogram import Bot, Dispatcher, executor, types

BOT_TOKEN = os.environ['TGB_TOKEN']

logging.basicConfig(level=logging.INFO)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/help` command.
    """
    await message.reply("Hi!\nI'm slaveork-bot\nPowered by aiogram.")

@dp.message_handler(regexp='(^cat[s]?$|puss)')
async def cats(message: types.Message):
    await message.reply("You know he's gone forever")

@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
