import json
import logging
import traceback

from settings.reader import admin_id


async def update_json_data(chat_id=None, video_id=None, title=None, artist=None):
    filename = f"current_{admin_id}.json"  # Чтение текущих данных из JSON файла
    try:
        with open(filename) as file:
            data = json.load(file)
            logging.debug(f"Update Json - {filename}.\n Old data: {data} ")
    except FileNotFoundError:
        data = {}
    except Exception as e:
        logging.error(f"Ошибка при открытии JSON-файла: {str(e)}")
        logging.error("Ошибка:\n", traceback.format_exc())

    # Обновление данных, если они переданы
    if chat_id is not None:
        data["chat_id"] = chat_id
    if video_id is not None:
        data["video_id"] = video_id
    if title is not None:
        data["title"] = title
    if artist is not None:
        data["artist"] = artist
    logging.debug(f"Update Json - {filename}.\n New data: {data} ")
    # Запись обновленных данных обратно в JSON файл
    with open(filename, "w") as file:
        json.dump(data, file)


async def edit_json_file(key_to_edit, new_value):
    filename = f"current_{admin_id}.json"
    try:
        # Чтение данных из файла
        with open(filename, encoding="utf-8") as file:
            data = json.load(file)
            logging.debug(f"Update Json - {filename}.\n Old data: {data} ")

        # Изменение данных
        if key_to_edit in data:
            data[key_to_edit] = new_value
            # print(data)
        else:
            logging.error(f"Ключ '{key_to_edit}' не найден в JSON-файле.")
        # print(data)
        # Запись обновленных данных обратно в файл
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

        logging.debug(f"Update Json - {filename}.\n New data: {data} ")
    except Exception as e:
        logging.error(f"Произошла ошибка при редактировании файла '{filename}': {e}")


async def read_json_data():
    filename = f"current_{admin_id}.json"
    try:
        with open(filename, encoding="utf-8") as file:
            data = json.load(file)
            chat_id = data.get("chat_id")
            video_id = data.get("video_id")
            title = data.get("title")
            artist = data.get("artist")
            return chat_id, video_id, title, artist
    except FileNotFoundError:
        return None
    except Exception as e:
        logging.error(f"Ошибка при чтении JSON-файла: {str(e)}")
        logging.error("Ошибка:\n", traceback.format_exc())
