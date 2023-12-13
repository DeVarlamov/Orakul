import os
from aiogram import Bot, types
from dotenv import load_dotenv

from core.utils.commands import set_commands
from core.keyboard.keybordbutton import keyboard
from core.db_config.db_config import Texts, session, Subscriber


load_dotenv()

ADMIN_ID = os.getenv('ADMIN_ID')


async def start_bot(bot: Bot):
    """Отправка сообщения в телеграмм о начале работы."""
    await bot.send_message(ADMIN_ID, text='Ракета взлетает')


async def end_bot(bot: Bot):
    """Отправка сообщения в телеграмм о конце работы."""
    await bot.send_message(ADMIN_ID, text='Ракета упала')


async def cmd_start(message: types.Message, bot: Bot):
    """Старт бота предсказаний."""
    await set_commands(bot)
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    user_lastname = message.from_user.last_name
    user_username = message.from_user.username
    subscriber = session.query(
        Subscriber).filter_by(chat_id=user_id).first()
    if subscriber:
        await bot.send_message(message.from_user.id,
                               f'Вы вернулись! {message.from_user.full_name}',
                               reply_markup=keyboard)
    else:
        subscriber = Subscriber(
            name=user_name, chat_id=user_id,
            lastname=user_lastname,
            user_username=user_username)
        session.add(subscriber)
        session.commit()
        await bot.send_message(
            message.from_user.id,
            f'Привет, '
            f'{message.from_user.first_name}! '
            'Добро пожаловать! Это "Вещий Ворон"',
            reply_markup=keyboard
            )


async def help_bot(message: types.Message, bot: Bot):
    await set_commands(bot)
    text = session.query(Texts).filter_by(id=1).first()
    await message.answer(f'Уважаемый! {message.from_user.full_name} '
                         '.\r\n Вещий Ворон'
                         f'.\r\n{text}'
                         )


async def admin_bot(message: types.Message, bot: Bot):
    await set_commands(bot)
    await message.answer(f'Уважаемый! {message.from_user.full_name} '
                         f'.\r\n Админка еще '
                         f'.\r\n в разработке у @Devarlamov! Но это не точно) '
                         )


async def get_photo(message: types.Message, bot: Bot):
    """Хедлер сохранения картинок."""
    await message.answer('Спасибо за картинку')
    file = await bot.get_file(message.photo[-1].file_id)
    await bot.download_file(file.file_path, 'image/photo.jpg')
