import asyncio
from aiogram import Bot
from aiogram.types import Message, FSInputFile
from sqlalchemy import func
from core.constant import CART_VORON
from core.db_config.db_config import Stikers_Voron, Voron_Speak, session
from core.keyboard.keybordbutton import keyboard_future_layouts
from utils import get_random_card


async def future_layouts(message: Message):
    await message.reply("окей, что ты хочешь узнать?",
                        reply_markup=keyboard_future_layouts)


async def recommendations(message: Message, bot: Bot):
    """Хедлер Общее предсказание на день (Таро)"""
    await message.answer('Погружение в астрал 🧛‍♀️🧛‍♀️🧛‍♀️')
    await asyncio.sleep(1)
    card, pack = get_random_card(CART_VORON)
    photo = FSInputFile(card,)
    stikers = session.query(
        Stikers_Voron).order_by(func.random()).first().name
    await message.answer_sticker(stikers)
    await asyncio.sleep(3)
    await bot.send_photo(message.chat.id, photo, caption=pack,
                         reply_markup=keyboard_future_layouts)


async def recommendations_day(message: Message):
    result = session.query(Voron_Speak).order_by(func.random()).first()
    await message.answer('Погружение в астрал 🧛‍♀️🧛‍♀️🧛‍♀️')
    await asyncio.sleep(1)
    stikers = session.query(
        Stikers_Voron).order_by(func.random()).first().name
    await message.answer_sticker(stikers)
    await asyncio.sleep(3)
    await message.reply(f"{result}",
                        reply_markup=keyboard_future_layouts)
