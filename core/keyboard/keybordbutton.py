from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


keyboard = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(
            text='Шар предсказаний (да/нет)'
        ),
        KeyboardButton(
            text='Расклады на любовь и отношения'
        ),
    ],
    [
        KeyboardButton(
            text='Расклады на денежные вопросы'
        ),
        KeyboardButton(
            text='Расклады на будущее'
        ),
    ],
    [
        KeyboardButton(
            text='Платные услуги'
        ),
    ]
], resize_keyboard=True, input_field_placeholder='Выбери кнопку ⬇️'
                                     )

keyboard_ball = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(
            text='🧙🏻‍♀️Menu'
        ),
    ],
], resize_keyboard=True, input_field_placeholder='Выбери кнопку ⬇️'
                                     )

keyboard_balls = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(
            text='отмена'
        ),
    ],
], resize_keyboard=True, input_field_placeholder='Напиши свой вопрос'
                                     )


keyboard_love_menu = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(
            text='Любит/не любит'
        ),
        KeyboardButton(
            text='Есть ли будущее у этих отношений?'
        ),
    ],
    [
        KeyboardButton(
            text='Чего ждать в любви с этим человеком?'
        ),
        KeyboardButton(
            text='Кто моя судьба?'
        ),
    ],
    [
        KeyboardButton(
            text='🧙🏻‍♀️Menu'
        ),
    ],
], resize_keyboard=True, input_field_placeholder='Выбери кнопку ⬇️'
                                     )


keyboard_love_and_not = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(
            text='Любит/не любит'
        ),
        KeyboardButton(
            text='🧙🏻‍♀️Menu'
        ),
    ],
], resize_keyboard=True, input_field_placeholder='Выбери кнопку ⬇️'
                                     )


keyboard_money = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(
            text='Найду ли я работу?'
        ),
    ],
    [
        KeyboardButton(
            text='Финансовый прогноз на неделю (Таро)'
        ),
    ],
    [
        KeyboardButton(
            text='🧙🏻‍♀️Menu'
        ),
    ]
], resize_keyboard=True, input_field_placeholder='Выбери кнопку ⬇️'
                                     )


keyboard_future_layouts = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(
            text='Совет Вещего Ворона на неделю.'
        ),
    ],
    [
        KeyboardButton(
            text='Общее предсказание на день (Таро)'
        ),
    ],
    [
        KeyboardButton(
            text='🧙🏻‍♀️Menu'
        ),
    ]
], resize_keyboard=True, input_field_placeholder='Выбери кнопку ⬇️'
                                     )

keyboard_pay = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(
            text='Большой расклад на месяц (Оракул Ленорман) 1500 руб.'
        ),
        KeyboardButton(
            text='Сложный вопрос (Цыганский оракул) 1200 руб.'
        ),
    ],
    [
        KeyboardButton(
            text='Любой вопрос о чувствах/отношениях (Таро) 1000 руб.'
        ),
        KeyboardButton(
            text='Узнать будущее (Цыганский оракул) 1000 руб.'
        ),
    ],
    [
        KeyboardButton(
            text='В чем мое предназначение? (Старшие Арканы Таро) 700 руб.'
        ),
        KeyboardButton(
            text='🧙🏻‍♀️Menu'
        ),
    ]
], resize_keyboard=True, input_field_placeholder='Выбери кнопку ⬇️'
                                     )

keyboard_after_pay = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(
            text='Оставить коментарии к заказу'
        ),
    ],
    [
        KeyboardButton(
            text='🧙🏻‍♀️Menu'
        ),
    ]
], resize_keyboard=True, input_field_placeholder='Выбери кнопку ⬇️'
                                     )
