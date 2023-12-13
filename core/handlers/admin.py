# from aiogram.types import Message


# @dp.message(F.text == 'Admin_Taro')
# async def admin(message: Message):
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