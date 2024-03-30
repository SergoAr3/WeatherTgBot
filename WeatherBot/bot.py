import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.filters import Command, CommandObject
from OpenWeatherAPI import get_weather
import logging
from os import getenv
from dotenv import load_dotenv

load_dotenv()
logging.basicConfig(level=logging.INFO)

bot = Bot(token=getenv('BOT_TOKEN'), parse_mode='HTML')
dp = Dispatcher()


@dp.message(Command('start'))
async def start(message: Message):
    await message.answer(
        f'Привет, <b>{message.from_user.first_name}!</b>\nЧтобы получить текущую погоду, просто напишите мне название вашего города!')

@dp.message()
async def weather(message: Message):
    city = message.text
    try:
        await message.answer(get_weather(city))
    except KeyError:
        await message.answer('Введите корректное название города!')



async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
