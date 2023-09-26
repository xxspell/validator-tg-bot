from aiogram import types
from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


def default_keyboard():
    kb = [
        [types.KeyboardButton(text="Трек"),
         types.KeyboardButton(text="Стаистика")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True,
                                         input_field_placeholder="♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥")

    return keyboard


def manage_track() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(text="Верно", callback_data="approve"), )
    builder.add(types.InlineKeyboardButton(text="Изменить название", callback_data="edit_name"), )
    builder.add(types.InlineKeyboardButton(text="Изменить исполнителя", callback_data="edit_artist"), )
    builder.add(types.InlineKeyboardButton(text="Удалить", callback_data="delete"), )
    builder.adjust(2)
    return builder.as_markup(resize_keyboard=True)
