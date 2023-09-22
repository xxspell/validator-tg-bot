import asyncio
from aiogram import Bot, Dispatcher

from settings.reader import bot_token
from handlers import different_types, track


# Запуск бота
async def main():
    bot = Bot(token=bot_token, parse_mode="HTML")
    dp = Dispatcher()

    dp.include_routers(different_types.router, track.router)
    # Альтернативный вариант регистрации роутеров по одному на строку
    # dp.include_router(questions.router)
    # dp.include_router(different_types.router)

    # Запускаем бота и пропускаем все накопленные входящие
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Bye-Bye. CTRL + C')
    # finally:
    #     print('ddd')
    #     sys.exit(0)
