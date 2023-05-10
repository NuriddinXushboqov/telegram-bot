import re

from aiogram import types
from aiogram.dispatcher.filters.builtin import Command
from loader import dp


@dp.message_handler(Command('til'))
async def changeLanguage(message: types.Message):
    arg = message.get_command()
    await message.answer(f"{arg} o'zgardi")


@dp.message_handler(Command(['shahar', 'davlat']))
async def changeLanguage(message: types.Message):
    arg = message.get_command()
    await message.answer(f"{arg} o'zgardi")
