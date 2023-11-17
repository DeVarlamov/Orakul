import asyncio
from aiogram import types
from sqlalchemy import func
from core.db_config.db_config import Stikers_for_ball, YesAndNo, session
from core.keyboard.keybordbutton import keyboard_ball


async def ball_predictor(message: types.Message):
    """Хедлер вопроса."""
    await message.reply("окей, задумай вопрос",
                        reply_markup=keyboard_ball)


async def yes_or_no(message: types.Message):
    """Хедлер ответа на вопрос."""
    result = session.query(YesAndNo).order_by(func.random()).first()
    await message.answer('Cвязь с космосом 🕣🕤🕥')
    await asyncio.sleep(1)
    stikers = session.query(
        Stikers_for_ball).order_by(func.random()).first().name
    await message.answer_sticker(stikers)
    await asyncio.sleep(3)
    await message.reply(f'{result}',
                        reply_markup=keyboard_ball)
