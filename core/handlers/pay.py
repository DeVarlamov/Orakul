import os
from aiogram import Bot
from aiogram.types import Message, LabeledPrice, PreCheckoutQuery
from core.keyboard.keybordbutton import keyboard_pay
from dotenv import load_dotenv


load_dotenv()

BANK_TOKEN = os.getenv('BANK_TOKEN')


async def the_great_oracle(message: Message, bot: Bot):
    """Большой расклад на месяц (Оракул Ленорман) 1500 руб."""
    await bot.send_invoice(
        chat_id=message.chat.id,
        title='Большой расклад на месяц (Оракул Ленорман)',
        description='Узнай свое будущее и все такое',
        payload='Payload a bot',
        provider_token=BANK_TOKEN,
        currency='rub',
        prices=[
            LabeledPrice(
                label='Большой расклад на месяц (Оракул Ленорман)',
                amount=150000
                )
        ],
        max_tip_amount=40000,
        suggested_tip_amounts=[15000, 20000, 30000, 40000],
        start_parameter='nztcoder',
        provider_data=None,
        photo_url='https://www.magical-life.ru/wp-content/uploads/2022/06/lenorman-1-1.jpg',
        photo_size=100,
        photo_width=800,
        photo_height=450,
        need_name=True,
        need_phone_number=True,
        need_email=True,
        need_shipping_address=False,
        send_phone_number_to_provider=False,
        is_flexible=False,
        disable_notification=False,
        protect_content=False,
        reply_to_message_id=None,
        allow_sending_without_reply=True,
        reply_markup=None,
        request_timeout=20,
        )


async def difficult_question(message: Message, bot: Bot):
    """Сложный вопрос (Цыганский оракул) 1200 руб."""
    await bot.send_invoice(
        chat_id=message.chat.id,
        title='Сложный вопрос (Цыганский оракул)',
        description='В картах ответ ты получишь',
        payload='Payload a bot',
        provider_token=BANK_TOKEN,
        currency='rub',
        prices=[
            LabeledPrice(
                label='Сложный вопрос (Цыганский оракул)',
                amount=120000
                )
        ],
        max_tip_amount=40000,
        suggested_tip_amounts=[15000, 20000, 30000, 40000],
        start_parameter='nztcoder',
        provider_data=None,
        photo_url='https://magistika.com/uploads/files/0_103.jpg',
        photo_size=100,
        photo_width=800,
        photo_height=450,
        need_name=True,
        need_phone_number=True,
        need_email=True,
        need_shipping_address=False,
        send_phone_number_to_provider=False,
        is_flexible=False,
        disable_notification=False,
        protect_content=False,
        reply_to_message_id=None,
        allow_sending_without_reply=True,
        reply_markup=None,
        request_timeout=20,
        )


async def question_feelings(message: Message, bot: Bot):
    """Любой вопрос о чувствах/отношениях (Таро) 1000 руб."""
    await bot.send_invoice(
        chat_id=message.chat.id,
        title='Любой вопрос о чувствах/отношениях (Таро)',
        description='В картах ответ ты получишь',
        payload='Payload a bot',
        provider_token=BANK_TOKEN,
        currency='rub',
        prices=[
            LabeledPrice(
                label='Любой вопрос о чувствах/отношениях (Таро)',
                amount=100000
                )
        ],
        max_tip_amount=100000,
        suggested_tip_amounts=[1500, 2000, 3000, 4000],
        start_parameter='nztcoder',
        provider_data=None,
        photo_url='https://www.magical-life.ru/wp-content/uploads/2022/05/love2.jpg',
        photo_size=100,
        photo_width=800,
        photo_height=450,
        need_name=True,
        need_phone_number=True,
        need_email=True,
        need_shipping_address=False,
        send_phone_number_to_provider=False,
        is_flexible=False,
        disable_notification=False,
        protect_content=False,
        reply_to_message_id=None,
        allow_sending_without_reply=True,
        reply_markup=None,
        request_timeout=20,
        )


async def learn_the_future(message: Message, bot: Bot):
    """Узнать будущее (Цыганский оракул) 1000 руб"""
    await bot.send_invoice(
        chat_id=message.chat.id,
        title='Узнать будущее (Цыганский оракул)',
        description='будет ли у тебя сегодня секс',
        payload='Payload a bot',
        provider_token=BANK_TOKEN,
        currency='rub',
        prices=[
            LabeledPrice(
                label='Узнать будущее (Цыганский оракул)',
                amount=100000
                )
        ],
        max_tip_amount=100000,
        suggested_tip_amounts=[1500, 2000, 3000, 4000],
        start_parameter='nztcoder',
        provider_data=None,
        photo_url='https://irecommend.ru/sites/default/files/imagecache/copyright1/user-images/896730/PXNgXQsUaT4LiN1TIUwAw.JPG',
        photo_size=100,
        photo_width=800,
        photo_height=450,
        need_name=True,
        need_phone_number=True,
        need_email=True,
        need_shipping_address=False,
        send_phone_number_to_provider=False,
        is_flexible=False,
        disable_notification=False,
        protect_content=False,
        reply_to_message_id=None,
        allow_sending_without_reply=True,
        reply_markup=None,
        request_timeout=20,
        )


async def destiny(message: Message, bot: Bot):
    """В чем мое предназначение? (Старшие Арканы Таро) 700 руб"""
    await bot.send_invoice(
        chat_id=message.chat.id,
        title='В чем мое предназначение? (Старшие Арканы Таро)',
        description='Узнай станешь ли ты хокаге',
        payload='Payload a bot',
        provider_token=BANK_TOKEN,
        currency='rub',
        prices=[
            LabeledPrice(
                label='В чем мое предназначение? (Старшие Арканы Таро))',
                amount=70000
                )
        ],
        max_tip_amount=60000,
        suggested_tip_amounts=[10000, 20000, 30000, 40000],
        start_parameter='nztcoder',
        provider_data=None,
        photo_url='https://static.tildacdn.com/tild6437-3363-4962-a431-306335633439/2.jpg',
        photo_size=100,
        photo_width=800,
        photo_height=450,
        need_name=True,
        need_phone_number=True,
        need_email=True,
        need_shipping_address=False,
        send_phone_number_to_provider=False,
        is_flexible=False,
        disable_notification=False,
        protect_content=False,
        reply_to_message_id=None,
        allow_sending_without_reply=True,
        reply_markup=None,
        request_timeout=20,
        )


async def pre_checkout_qwery(pre_checkout_qwery: PreCheckoutQuery, bot: Bot):
    await bot.answer_pre_checkout_query(pre_checkout_qwery.id, ok=True)


async def successfull_payment(message: Message):
    msg = f'Спасибо за покупку {message.successful_payment.total_amount // 100} {message.successful_payment.currency}.\r\n Наш менеджер с вами свяжется'
    await message.answer(msg)


async def pay_menu(message: Message, bot: Bot):
    """Хедлер обработки платного меню"""
    await message.reply("Выберите подходящую услугу",
                        reply_markup=keyboard_pay)
