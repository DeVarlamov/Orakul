import asyncio
import logging
import os
from aiogram import F
from logging.handlers import RotatingFileHandler
from aiogram.filters import Command
from aiogram import Bot, Dispatcher
from apps.ball_predictions.ball import ball_predictor, yes_or_no
from apps.relationship_layouts.layouts import (
    doom,
    love_predictor,
    love_yes_or_no,
    the_future_with_man,
    this_relationship
    )

from core.handlers.basic import (
    cmd_start,
    end_bot,
    start_bot,
    get_photo
    )


logger = logging.getLogger()
logger.setLevel(logging.INFO)
file_handler = RotatingFileHandler(
    'logfile.txt',)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

logger.info('Это сообщение журнала')
logger.info('Еще одно сообщение журнала')


async def start():
    bot = Bot(token=os.getenv('TOKEN'), parse_mode='HTML')
    dp = Dispatcher()
# =================== Регестрация Хедлеров ================
    dp.startup.register(start_bot)
    dp.shutdown.register(end_bot)

    dp.message.register(get_photo, F.photo)

    dp.message.register(cmd_start, Command(commands=['start', 'Menu']))
    dp.message.register(ball_predictor, F.text == "Шар предсказаний (да/нет)")
    dp.message.register(yes_or_no, F.text == "Узнать ответ")
    dp.message.register(
        love_predictor, F.text == 'Расклады на любовь и отношения')
    dp.message.register(love_yes_or_no, F.text == 'Любит/не любит')
    dp.message.register(doom, F.text == 'Кто моя судьба?')
    dp.message.register(this_relationship,
                        F.text == 'Есть ли будущее у этих отношений?')
    dp.message.register(the_future_with_man,
                        F.text == 'Чего ждать в любви с этим человеком?')

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(start())

# # ===================== Методы Расклады на денежные вопросы ================
# @dp.message(F.text == "Расклады на денежные вопросы")
# async def money_issues(message: types.Message):
#     kb = [
#         [types.KeyboardButton(text="Найду ли я работу?")],
#         [types.KeyboardButton(text="Финансовый прогноз на неделю (Таро)")],
#         [types.KeyboardButton(text="Главное меню")],
#     ]
#     keyboard = types.ReplyKeyboardMarkup(
#         keyboard=kb,
#         resize_keyboard=True,)
#     await message.reply("окей, задумай вопрос",
#                         reply_markup=keyboard)


# @dp.message(F.text == "Найду ли я работу?")
# async def job_search(message: types.Message):
#     kb = [
#         [types.KeyboardButton(text="Главное меню")],
#     ]
#     keyboard = types.ReplyKeyboardMarkup(
#         keyboard=kb,
#         resize_keyboard=True,)
#     result = Random_choise.get_random_str(WORK_BELT)
#     await message.answer('Сканирования данных приносящих прибыль🤑🤑🤑')
#     await asyncio.sleep(1)
#     GIF = Random_choise.get_random_smails(WORK_BELT_GIF)
#     await message.answer_sticker(GIF)
#     await asyncio.sleep(3)
#     await message.reply(f'"{result}"',
#                         reply_markup=keyboard)


# @dp.message(F.text == "Финансовый прогноз на неделю (Таро)")
# async def job_search1(message: types.Message):
#     kb = [
#         [types.KeyboardButton(text="Главное меню")],
#     ]
#     keyboard = types.ReplyKeyboardMarkup(
#         keyboard=kb,
#         resize_keyboard=True,)
#     await message.answer('Запрос к судьбе 🎴🎴🎴')
#     await asyncio.sleep(1)
#     card, pack = get_random_card(CART)
#     photo = FSInputFile(card,)
#     GIF = Random_choise.get_random_smails(WORK_BELT_GIF)
#     await message.answer_sticker(GIF)
#     await asyncio.sleep(3)
#     await bot.send_photo(message.chat.id, photo, caption=pack,
#                          reply_markup=keyboard)

# # ===================Расклады на будующее меню ===========================


# @dp.message(F.text == 'Расклады на будущее')
# async def future_layouts(message: types.Message):
#     kb = [
#         [types.KeyboardButton(text="Совет Вещего Ворона на неделю.")],
#         [types.KeyboardButton(text="Общее предсказание на день (Таро)")],
#         [types.KeyboardButton(text="Главное меню")],
#     ]
#     keyboard = types.ReplyKeyboardMarkup(
#         keyboard=kb,
#         resize_keyboard=True,)
#     await message.reply("окей, что ты хочешь узнать?",
#                         reply_markup=keyboard)


# # ======================== Расклады на будующее ===========================
# @dp.message(F.text == 'Общее предсказание на день (Таро)')
# async def recommendations(message: types.Message):
#     kb = [
#         [types.KeyboardButton(text="Главное меню")],
#     ]
#     keyboard = types.ReplyKeyboardMarkup(
#         keyboard=kb,
#         resize_keyboard=True,)
#     await message.answer('Запрос к судьбе 🎴🎴🎴')
#     await asyncio.sleep(1)
#     card, pack = get_random_card(CART_VORON)
#     photo = FSInputFile(card,)
#     GIF = Random_choise.get_random_smails(WORK_BELT_GIF)
#     await message.answer_sticker(GIF)
#     await asyncio.sleep(3)
#     await bot.send_photo(message.chat.id, photo, caption=pack,
#                          reply_markup=keyboard)


# @dp.message(F.text == 'Совет Вещего Ворона на неделю.')
# async def recommendations_day(message: types.Message):
#     kb = [
#         [types.KeyboardButton(text="Главное меню")],
#     ]
#     keyboard = types.ReplyKeyboardMarkup(
#         keyboard=kb,
#         resize_keyboard=True,)
#     result = Random_choise.get_random_str(BOLS_STORIS)
#     await message.answer('Cвязь с космосом 🕣🕤🕥')
#     await asyncio.sleep(1)
#     GIF = Random_choise.get_random_smails(GIF_FOR_BOLL)
#     await message.answer_sticker(GIF)
#     await asyncio.sleep(3)
#     await message.reply(f'твой ответ "{result}"',
#                         reply_markup=keyboard)


# # ====================== Админка ===================================

# @dp.message(F.text == 'Admin_Taro')
# async def admin(message: types.Message):
#     admin_panel = [
#         [types.KeyboardButton(text='Добавить кoнтeнт')],
#         [types.KeyboardButton(text='Добавить блогг')],
#     ]
#     keyboard_admin = types.ReplyKeyboardMarkup(
#         keyboard=admin_panel,
#         resize_keyboard=True,
#     )
#     if message.from_user.id == int(os.getenv('ADMIN_ID')):
#         await message.answer('Вы в меню админа',
#                              reply_markup=keyboard_admin)
#     else:
#         await message.reply('В доступе отказанно')


# @dp.message(F.text == 'Добавить блогг')
# async def admin(message: types.Message):
#     admin_panel = [
#         [types.KeyboardButton(text='Добавить блогг')],
#         [types.KeyboardButton(text="Главное меню")]
#     ]
#     keyboard_admin = types.ReplyKeyboardMarkup(
#         keyboard=admin_panel,
#         resize_keyboard=True,
#     )
#     if message.from_user.id == int(os.getenv('ADMIN_ID')):
#         chat_ids = session.query(Subscriber.chat_id).all()
#         for chat_id in chat_ids:
#             try:
#                 chat_id = int(chat_id[0])
#                 await bot.send_message(chat_id,
#                                        message.text,
#                                        reply_markup=keyboard_admin)
#                 logger.info('сообщение отправленно')
#             except Exception as e:
#                 logging.info(
#                     f'Не удалось отправить'
#                     f'сообщение пользователю {chat_id}: {str(e)}')
#         await message.answer('Сообщение отправлено всем пользователям')
#         await message.answer('Вы в меню админа', reply_markup=keyboard_admin)
#     else:
#         await message.reply('В доступе отказано')


# ==================== Запуск ========================================
