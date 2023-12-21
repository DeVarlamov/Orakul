import asyncio
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from sqlalchemy import func
from core.db_config.db_config import Stikers_for_ball, YesAndNo, session
from core.keyboard.keybordbutton import keyboard_balls, keyboard
from core.utils.statesform import StateForm


async def ball_predictor(message: Message, state: FSMContext):
    """Хедлер вопроса."""
    await message.reply("Напиши мне 1 вопрос который тебя интересует",
                        reply_markup=keyboard_balls)
    await state.set_state(StateForm.GET_TEXT)


async def yes_or_no(message: Message, state: FSMContext):
    """Хедлер ответа на вопрос."""
    if message.text == 'отмена':
        await state.clear()
        await message.answer('Вы вернулись в меню', reply_markup=keyboard)
    else:
        result = session.query(YesAndNo).order_by(func.random()).first()
        await message.answer('Cвязь с космосом 🕣🕤🕥')
        await asyncio.sleep(1)
        stikers = session.query(
            Stikers_for_ball).order_by(func.random()).first().name
        await message.answer_sticker(stikers)
        await asyncio.sleep(3)
        await message.reply(f'{result}'
                            '.\r\n ⬅️ Вы вернулись в меню',
                            reply_markup=keyboard)
    await state.clear()
