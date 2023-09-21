from aiogram import types


def default_keyboard():
    kb = [
        [types.KeyboardButton(text="Трек"),
         types.KeyboardButton(text="Стаистика")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True,
                                         input_field_placeholder="♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥")

    return keyboard