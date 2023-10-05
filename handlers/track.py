from contextlib import suppress

from aiogram import F, Router, types
from aiogram.exceptions import TelegramBadRequest
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from handlers.filters import Admin
from keyboards.for_questions import manage_track
from tools.json_t import edit_json_file, read_json_data
from tools.message import save_message_id
from tools.sql import connection, get_data_db

router = Router()


async def message_track():
    chat_id, video_id, title, artist = await read_json_data()
    message = f'Название: <code>{title}</code>\nИсполнитель: <code>{artist}</code>\n<a href="https://www.youtube.com/watch?v={video_id}">link</a>'
    return message, chat_id, video_id, title, artist


class AskName(StatesGroup):
    name = State()


class AskArtist(StatesGroup):
    name = State()


@router.message(Admin(), Command("track"))
@router.message(Admin(), F.text.lower() == "трек")
async def send_update_message(message: types.Message):
    await get_data_db()
    data = await message_track()
    await message.answer(
        data[0],
        reply_markup=manage_track(),
        disable_web_page_preview=False,
    )
    await save_message_id(data[2])


@router.callback_query(F.data == "approve")
async def confirm_data(callback: types.CallbackQuery):
    chat_id, video_id, title, artist = await read_json_data()

    # print('Подтверждаю данные')
    try:
        cursor = connection.cursor()
        # Обновляем запись в таблице videos_untrusted
        cursor.execute(
            "UPDATE videos_untrusted SET checked = 1 WHERE video_id = %s", (video_id,)
        )
        connection.commit()

        # Добавляем или обновляем запись в таблице videos
        cursor.execute(
            "INSERT INTO videos (title, artist, video_id) VALUES (%s, %s, %s) ON DUPLICATE KEY UPDATE title = VALUES("
            "title)",
            (title, artist, video_id),
        )
        connection.commit()
        with suppress(TelegramBadRequest):
            await callback.message.edit_text(
                "Окей, принял. Введите /track чтобы продолжить"
            )
    except Exception as e:
        print(f"Ошибка при обновлении данных: {str(e)}")
        await callback.message.answer("Произошла ошибка при обновлении данных")


@router.callback_query(F.data == "edit_name")
async def edit_title(callback: types.CallbackQuery, state: FSMContext) -> None:
    # chat_id, video_id, title, artist = await read_json_data()
    await state.set_state(AskName.name)
    data = await message_track()
    with suppress(TelegramBadRequest):
        await callback.message.edit_text(
            text=f"Укажите название(<code>{data[3]}</code>):", reply_markup=None
        )
        # f"Укажите число: {new_value}",


@router.message(AskName.name)
async def get_address(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    # print(message.text)
    data = await state.get_data()
    # print(data)
    await edit_json_file("title", data["name"])
    # print(data)
    await state.clear()
    data = await message_track()
    await message.answer(
        data[0],
        reply_markup=manage_track(),
        disable_web_page_preview=False,
    )


@router.callback_query(F.data == "edit_artist")
async def edit_title(callback: types.CallbackQuery, state: FSMContext) -> None:
    # chat_id, video_id, title, artist = await read_json_data()
    await state.set_state(AskArtist.name)
    data = await message_track()
    with suppress(TelegramBadRequest):
        await callback.message.edit_text(
            text=f"Укажите исполнителя(<code>{data[4]}</code>:", reply_markup=None
        )
        # f"Укажите число: {new_value}",


@router.message(AskArtist.name)
async def get_address(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    # print(message.text)
    data = await state.get_data()
    # print(data)
    await edit_json_file("artist", data["name"])
    # print(data)
    await state.clear()
    data = await message_track()
    await message.answer(
        data[0],
        reply_markup=manage_track(),
        disable_web_page_preview=False,
    )


@router.callback_query(F.data == "delete")
async def confirm_data(callback: types.CallbackQuery):
    chat_id, video_id, title, artist = await read_json_data()

    # print('Удаляю данные')
    try:
        cursor = connection.cursor()
        # Обновляем запись в таблице videos_untrusted
        cursor.execute(
            "UPDATE videos_untrusted SET checked = 1 WHERE video_id = %s", (video_id,)
        )
        connection.commit()
        with suppress(TelegramBadRequest):
            await callback.message.edit_text(
                "Окей, удалил. Введите /track чтобы продолжить"
            )
    except Exception as e:
        print(f"Ошибка при обновлении данных: {str(e)}")
        await callback.message.answer("Произошла ошибка при обновлении данных")
