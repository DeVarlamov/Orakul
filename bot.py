import asyncio
import logging
import os
from logging.handlers import RotatingFileHandler
from aiogram.filters import Command
from aiogram import Bot, Dispatcher, F
from core.constant import BIG_ORACUL, DESTINY, DIGGICULT_QUESTION, LEARN_FUTURE, QUESTION_FEELINGS
from core.handlers.ball import (
    ball_predictor,
    yes_or_no,
    )
# from core.handlers.colback import selekt_help
from core.handlers.layouts import (
    doom,
    love_predictor,
    love_yes_or_no,
    the_future_with_man,
    this_relationship
    )

from core.handlers.basic import (
    cmd_start,
    end_bot,
    help_bot,
    start_bot,
    get_photo
    )

from core.handlers.maney_qwestion import (
    money_issues,
    job_search,
    job_search_forecast
    )

from core.handlers.layouts_future import (
    future_layouts,
    recommendations,
    recommendations_day)
from core.handlers.pay import (
    destiny,
    difficult_question,
    learn_the_future,
    question_feelings,
    the_great_oracle,
    pay_menu,
    pre_checkout_qwery,
    successfull_payment
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

    dp.message.register(cmd_start, Command(commands=['start',]))
    dp.message.register(help_bot, Command(commands=['help',]))
    dp.message.register(cmd_start, F.text == '🧙🏻‍♀️Menu')
    dp.message.register(ball_predictor, F.text == "Шар предсказаний (да/нет)")
    dp.message.register(pay_menu, F.text == 'Платные услуги')
    dp.message.register(the_great_oracle, F.text == BIG_ORACUL)
    dp.message.register(difficult_question, F.text == DIGGICULT_QUESTION)
    dp.message.register(question_feelings, F.text == QUESTION_FEELINGS)
    dp.message.register(learn_the_future, F.text == LEARN_FUTURE)
    dp.message.register(destiny, F.text == DESTINY)
    dp.pre_checkout_query.register(pre_checkout_qwery)
    dp.message.register(successfull_payment,  F.successful_payment)
    dp.message.register(yes_or_no, F.text == "Узнать ответ")
    dp.message.register(
        love_predictor, F.text == 'Расклады на любовь и отношения')
    dp.message.register(love_yes_or_no, F.text == 'Любит/не любит')
    dp.message.register(doom, F.text == 'Кто моя судьба?')
    dp.message.register(this_relationship,
                        F.text == 'Есть ли будущее у этих отношений?')
    dp.message.register(the_future_with_man,
                        F.text == 'Чего ждать в любви с этим человеком?')
    dp.message.register(money_issues, F.text == "Расклады на денежные вопросы")
    dp.message.register(job_search, F.text == "Найду ли я работу?")
    dp.message.register(job_search_forecast,
                        F.text == "Финансовый прогноз на неделю (Таро)")
    dp.message.register(future_layouts, F.text == 'Расклады на будущее')
    dp.message.register(recommendations,
                        F.text == 'Общее предсказание на день (Таро)')
    dp.message.register(recommendations_day,
                        F.text == 'Совет Вещего Ворона на неделю.')

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(start())
