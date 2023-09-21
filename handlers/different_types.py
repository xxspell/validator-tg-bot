from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command, CommandStart
from keyboards.for_questions import default_keyboard
router = Router()


@router.message(CommandStart())
@router.message(F.text.casefold() == "start")
async def start(message: Message):
    await message.answer("Доступ разрешён, выберете действие(статистика не сделана):", reply_markup=default_keyboard())
