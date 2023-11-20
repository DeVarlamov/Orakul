import asyncio
from aiogram import Bot
from aiogram.types import Message, FSInputFile
from sqlalchemy import func
from core.constant import CART

from core.keyboard.keybordbutton import keyboard_money
from core.db_config.db_config import session, Work_Belt, Stikers_Work_Belt
from utils import get_random_card


async def money_issues(message: Message):
    """Хедлерс перехада в меню вопросам по финансам"""
    await message.reply("окей, задумай вопрос",
                        reply_markup=keyboard_money)


async def job_search(message: Message):
    """Хедлер с ответом Найду ли я работу?"""
    result = session.query(Work_Belt).order_by(func.random()).first()
    await message.answer('Сканирования данных приносящих прибыль🤑🤑🤑')
    await asyncio.sleep(1)
    stikers = session.query(
        Stikers_Work_Belt).order_by(func.random()).first().name
    await message.answer_sticker(stikers)
    await asyncio.sleep(3)
    await message.reply(f'"{result}"',
                        reply_markup=keyboard_money)


async def job_search_forecast(message: Message, bot: Bot):
    """Хедлер Финансовый прогноз на неделю (Таро)"""
    await message.answer('Запрос к судьбе 🎴🎴🎴')
    await asyncio.sleep(1)
    card, pack = get_random_card(CART)
    photo = FSInputFile(card,)
    stikers = session.query(
        Stikers_Work_Belt).order_by(func.random()).first().name
    await message.answer_sticker(stikers)
    await asyncio.sleep(3)
    await bot.send_photo(message.chat.id, photo, caption=pack,
                         reply_markup=keyboard_money)
