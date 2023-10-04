import logging
import traceback

import pymysql

from settings.reader import admin_id, sql_database, sql_host, sql_password, sql_user
from tools.json_t import read_json_data, update_json_data

connection = pymysql.connect(
    host=sql_host, user=sql_user, password=sql_password, database=sql_database
)


async def get_data_db():
    while True:
        try:
            logging.debug("Get data from videos_untrusted")
            cursor = connection.cursor()
            # Получаем самую старую запись, у которой checked = 0
            cursor.execute(
                "SELECT * FROM videos_untrusted WHERE checked = 0 ORDER BY time_listen LIMIT 1"
            )
            row = cursor.fetchone()
            if row:
                video_id, title, artist = row[3], row[1], row[2]
                chat_id = admin_id  # Замените на ID вашего чата
                await update_json_data(chat_id, video_id, title, artist)

                # Извлекаем переменные из словаря

                data = await read_json_data()
                # Проверьте, что данные были успешно получены, прежде чем их распаковать
                if data is not None:
                    chat_id, video_id, title, artist = data
                    # Далее обрабатывайте данные, как вам нужно
                else:
                    logging.error("Ошибка при получении данных из JSON.")
                return chat_id, video_id, title, artist

            else:
                logging.critical("mda")
        except Exception as e:
            logging.error(f"Ошибка при получении данных: {str(e)}")
            logging.error("Ошибка:\n", traceback.format_exc())
