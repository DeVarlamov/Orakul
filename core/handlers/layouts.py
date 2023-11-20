import asyncio
from aiogram import Bot
from aiogram.types import Message
from sqlalchemy import func
from core.keyboard.keybordbutton import (
    keyboard_love_menu,
    )
from core.db_config.db_config import (
    Future_Man,
    Subscriber,
    This_Relation,
    session,
    LoveYesAndNo,
    Stikers_for_love
    )


async def love_predictor(message: Message, bot: Bot):
    """Хедлер Меню расклада любви и отношений."""
    await message.reply("Окей, какие у тебя вопросы?",
                        reply_markup=keyboard_love_menu)


async def love_yes_or_no(message: Message):
    """Хедлер для ответа Любит/не любит"""
    result = session.query(LoveYesAndNo).order_by(func.random()).first()
    await message.answer('Cвязь с планетой любви 💓💓💓')
    await asyncio.sleep(1)
    stikers = session.query(
        Stikers_for_love).order_by(func.random()).first().name
    await message.answer_sticker(stikers)
    await asyncio.sleep(3)
    await message.reply(f'{result}',
                        reply_markup=keyboard_love_menu)


async def doom(message: Message):
    """Хедлер для ответа: Кто моя судьба?."""
    user_id = message.from_user.id
    result = session.query(Subscriber).order_by(func.random()).first()
    if result.chat_id == user_id:
        await message.reply(
            f'{message.from_user.first_name} вы ни кому не нужены 😕',
            reply_markup=keyboard_love_menu
            )
    else:
        await message.answer('Cвязь с Ларисой Гузеевой 💓💓💓')
        await asyncio.sleep(1)
        stikers = session.query(
            Stikers_for_love).order_by(func.random()).first().name
        await message.answer_sticker(stikers)
        await asyncio.sleep(3)
        await message.reply(f'Твоя судьба!'
                            f' @{result.user_username}',
                            reply_markup=keyboard_love_menu)


async def this_relationship(message: Message):
    """Хедлер для ответа есть ли будущее у отношений."""
    result = session.query(This_Relation).order_by(func.random()).first()
    await message.answer('Cвязь с планетой любви 💓💓💓')
    await asyncio.sleep(1)
    stikers = session.query(
            Stikers_for_love).order_by(func.random()).first().name
    await message.answer_sticker(stikers)
    await asyncio.sleep(3)
    await message.reply(f'{result}',
                        reply_markup=keyboard_love_menu)


async def the_future_with_man(message: Message):
    """Хедлер чего ждать с этим человеком?"""
    result = session.query(Future_Man).order_by(func.random()).first()
    await message.answer('Cвязь с планетой любви 💓💓💓')
    await asyncio.sleep(1)
    stikers = session.query(
            Stikers_for_love).order_by(func.random()).first().name
    await message.answer_sticker(stikers)
    await asyncio.sleep(3)
    await message.reply(f'{result}',
                        reply_markup=keyboard_love_menu)
