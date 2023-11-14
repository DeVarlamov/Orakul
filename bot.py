import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram import F
from constant import (
    BOLS_STORIS,
    FUTURE_MAN,
    GIF_FOR_BOLL,
    GIF_FOR_LOVE,
    LOVE_STORIS,
    THIS_RELATION,
    TOKEN,
    WORK_BELT,
    WORK_BELT_GIF
    )
from aiogram.types import URLInputFile
from utils import (
    Random_choise
    )

logging.basicConfig(level=logging.INFO)
bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    """Старт бота предсказаний."""
    kb = [
        [types.KeyboardButton(text='Шар предсказаний (да/нет)')],
        [types.KeyboardButton(text='Расклады на любовь и отношения')],
        [types.KeyboardButton(text='Расклады на денежные вопросы')],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,)
    await message.answer(
        f'Привет, {message.from_user.first_name}! '
        'Добро пожаловать! Это "Вещий Ворон"',
        reply_markup=keyboard
    )


@dp.message(F.text == "Главное меню")
async def menu_start(message: types.Message):
    """Меню."""
    kb = [
        [types.KeyboardButton(text="Шар предсказаний (да/нет)",
                              color='green')],
        [types.KeyboardButton(text='Расклады на любовь и отношения',
                              )],
        [types.KeyboardButton(text='Расклады на денежные вопросы')],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,)
    await message.answer(
        f'{message.from_user.first_name}! '
        'Вещий ворон подскажет',
        reply_markup=keyboard
    )

# =======================Методы Расклады отношений ==================


@dp.message(F.text == "Расклады на любовь и отношения")
async def love_predictor(message: types.Message):
    """Меню расклада любви и отношений."""
    kb = [
        [types.KeyboardButton(text="Любит/не любит")],
        [types.KeyboardButton(text="Есть ли будущее у этих отношений?")],
        [types.KeyboardButton(text='Чего ждать в любви с этим человеком?')]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,)
    await message.reply("Окей",
                        reply_markup=keyboard)


@dp.message(F.text == "Любит/не любит")
async def love_yes_or_no(message: types.Message):
    kb = [
        [types.KeyboardButton(text="Любит/не любит")],
        [types.KeyboardButton(text="Главное меню")],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,)
    result = Random_choise.get_random_str(LOVE_STORIS)
    await message.answer('Cвязь с планетой любви 💓💓💓')
    await asyncio.sleep(1)
    GIF = Random_choise.get_random_smails(GIF_FOR_LOVE)
    await message.answer_sticker(GIF)
    await asyncio.sleep(3)
    await message.reply(f'Ответ "{result}"',
                        reply_markup=keyboard)


@dp.message(F.text == 'Есть ли будущее у этих отношений?')
async def this_relationship(message: types.Message):
    kb = [
        [types.KeyboardButton(text="Главное меню")],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,)
    result = Random_choise.get_random_str(THIS_RELATION)
    await message.answer('Cвязь с планетой любви 💓💓💓')
    await asyncio.sleep(1)
    GIF = Random_choise.get_random_smails(GIF_FOR_LOVE)
    await message.answer_sticker(GIF)
    await asyncio.sleep(3)
    await message.reply(f'Ответ "{result}"',
                        reply_markup=keyboard)


@dp.message(F.text == 'Чего ждать в любви с этим человеком?')
async def the_future_with_man(message: types.Message):
    kb = [
        [types.KeyboardButton(text="Главное меню")],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,)
    result = Random_choise.get_random_str(FUTURE_MAN)
    await message.answer('Cвязь с планетой любви 💓💓💓')
    await asyncio.sleep(1)
    GIF = Random_choise.get_random_smails(GIF_FOR_LOVE)
    await message.answer_sticker(GIF)
    await asyncio.sleep(3)
    await message.reply(f'Ответ "{result}"',
                        reply_markup=keyboard)


# ====================== Методы шара предсказаний ===================
@dp.message(F.text == "Шар предсказаний (да/нет)")
async def ball_predictor(message: types.Message):
    kb = [
        [types.KeyboardButton(text="Узнать ответ")],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,)
    await message.reply("окей, задумай вопрос",
                        reply_markup=keyboard)


@dp.message(F.text == "Узнать ответ")
async def yes_or_no(message: types.Message):
    kb = [
        [types.KeyboardButton(text="Главное меню")],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,)
    result = Random_choise.get_random_str(BOLS_STORIS)
    await message.answer('Cвязь с космосом 🕣🕤🕥')
    await asyncio.sleep(1)
    GIF = Random_choise.get_random_smails(GIF_FOR_BOLL)
    await message.answer_sticker(GIF)
    await asyncio.sleep(3)
    await message.reply(f'твой ответ "{result}"',
                        reply_markup=keyboard)


# ===================== Методы Расклады на денежные вопросы ==================
@dp.message(F.text == "Расклады на денежные вопросы")
async def money_issues(message: types.Message):
    kb = [
        [types.KeyboardButton(text="Найду ли я работу?")],
        [types.KeyboardButton(text="Финансовый прогноз на неделю (Таро)")],
        [types.KeyboardButton(text="Главное меню")],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,)
    await message.reply("окей, задумай вопрос",
                        reply_markup=keyboard)


@dp.message(F.text == "Найду ли я работу?")
async def job_search(message: types.Message):
    kb = [
        [types.KeyboardButton(text="Главное меню")],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,)
    result = Random_choise.get_random_str(WORK_BELT)
    await message.answer('Сканирования данных приносящих прибыль🤑🤑🤑')
    await asyncio.sleep(1)
    GIF = Random_choise.get_random_smails(WORK_BELT_GIF)
    await message.answer_sticker(GIF)
    await asyncio.sleep(3)
    await message.reply(f'"{result}"',
                        reply_markup=keyboard)


@dp.message(F.text == "Финансовый прогноз на неделю (Таро)")
async def job_search1(message: types.Message):
    kb = [
        [types.KeyboardButton(text="Главное меню")],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,)
    image_from_url = URLInputFile("https://picsum.photos/seed/groosha/400/300")
    await message.answer_photo(
        image_from_url,
        caption="Изображение по ссылке",
        reply_markup=keyboard
    )


# ==================== Запуск ========================================
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
