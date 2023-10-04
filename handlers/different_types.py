from aiogram import F, Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from handlers.filters import Admin
from keyboards.for_questions import default_keyboard

router = Router()


@router.message(~Admin())
async def not_admin(message: Message):
    await message.answer_sticker(
        r"CAACAgIAAxkBAAIpR2UdZS6SZI_iSRh3j4w7Fn0vn8abAALTAAM8ilcakZtNoizuo7owBA"
    )
    await message.answer("@xxspell")


@router.message(Admin(), CommandStart())
@router.message(Admin(), F.text.casefold() == "start")
async def start(message: Message):
    await message.answer(
        "Доступ разрешён, выберете действие(статистика не сделана):",
        reply_markup=default_keyboard(),
    )
