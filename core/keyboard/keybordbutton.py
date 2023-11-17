from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, KeyboardButtonPollType


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
    ]
], resize_keyboard=True, input_field_placeholder='Выбери кнопку ⬇️'
                                     )

keyboard_ball = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(
            text='Узнать ответ'
        ),
        KeyboardButton(
            text='/Menu'
        ),
    ],
], resize_keyboard=True, input_field_placeholder='Выбери кнопку ⬇️'
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
            text='/Menu'
        ),
    ],
    [
        KeyboardButton(
            text='Чего ждать в любви с этим человеком?'
        ),
        KeyboardButton(
            text='Кто моя судьба?'
        ),
    ]
], resize_keyboard=True, input_field_placeholder='Выбери кнопку ⬇️'
                                     )


keyboard_love_and_not = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(
            text='Любит/не любит'
        ),
        KeyboardButton(
            text='/Menu'
        ),
    ],
], resize_keyboard=True, input_field_placeholder='Выбери кнопку ⬇️'
                                     )
