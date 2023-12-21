import asyncio
from aiogram import Bot
from aiogram.types import Message, FSInputFile
from datetime import datetime
from sqlalchemy import func
from core.constant import CART_VORON
from core.db_config.db_config import (
    Recommendations,
    Stikers_Voron,
    Voron_Speak,
    session
    )
from core.keyboard.keybordbutton import keyboard_future_layouts
from utils import get_random_card


async def future_layouts(message: Message, bot: Bot):
    await message.reply("окей, что ты хочешь узнать?",
                        reply_markup=keyboard_future_layouts)


async def recommendations(message: Message, bot: Bot):
    """Хедлер Общее предсказание на день (Таро)"""
    user_id = message.from_user.id
    current_time = datetime.now()
    subscriber = session.query(
        Recommendations).filter(Recommendations.chat_id == user_id).first()
    if subscriber and subscriber.last_prediction_time.date(
    ) == current_time.date():
        rep_path_card = subscriber.path_card
        rep_pack = subscriber.pack
        rep_photo = FSInputFile(rep_path_card)
        await message.answer(
            'Вы уже получали предсказание сегодня.'
            '\r\n  Вот оно еще раз!')
        await bot.send_photo(
            message.chat.id,
            rep_photo,
            caption=rep_pack,
            reply_markup=keyboard_future_layouts)
    else:
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
        if subscriber:
            subscriber.last_prediction_time = current_time
            subscriber.path_card = card
            subscriber.pack = pack
        else:
            new_subscriber = Recommendations(
                chat_id=user_id,
                last_prediction_time=current_time,
                path_card=card, pack=pack
                )
            session.add(new_subscriber)
        session.commit()


async def recommendations_week(message: Message):
    """ Предсказание на неделю"""
    result = session.query(Voron_Speak).order_by(func.random()).first()
    await message.answer('Погружение в астрал 🧛‍♀️🧛‍♀️🧛‍♀️')
    await asyncio.sleep(1)
    stikers = session.query(
        Stikers_Voron).order_by(func.random()).first().name
    await message.answer_sticker(stikers)
    await asyncio.sleep(3)
    await message.reply(f"{result}",
                        reply_markup=keyboard_future_layouts)
