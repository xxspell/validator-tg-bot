import logging
import traceback


async def save_message_id(message_id):
    try:
        with open("bot_data.txt", "w") as file:
            file.write(message_id)
    except Exception as e:
        logging.error(f"Ошибка при создания айди сообщения: {str(e)}")
        logging.error("Ошибка:\n", traceback.format_exc())
