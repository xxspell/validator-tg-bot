from aiogram import Router, F, types

from aiogram.filters import Command
from aiogram.fsm.state import StatesGroup, State

from keyboards.for_questions import manage_track
from tools.json_t import read_json_data, edit_json_file
from tools.sql import get_data_db, connection
from tools.message import save_message_id
from handlers.filters import Admin

router = Router()


class AskName(StatesGroup):
    name = State()


class AskArtist(StatesGroup):
    name = State()


@router.message(Admin(), Command('track'))
@router.message(Admin(), F.text.lower() == "трек")
async def send_update_message(message: types.Message):
    await get_data_db()

    chat_id, video_id, title, artist = await read_json_data()
    await message.answer(
        f"Название: {title}\nИсполнитель: {artist}\n<a href=\"https://www.youtube.com/watch?v={video_id}\">link</a>",
        reply_markup=manage_track(),
        disable_web_page_preview=False,
    )
    await save_message_id(video_id)
