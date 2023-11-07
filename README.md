# Телеграм-бот для проверки и коррекции данных
![Трек](https://raw.githubusercontent.com/xxspell/validator-tg-bot/service/track.png)

Этот бот разработан для удобной проверки и коррекции музыкальных данных. Он предоставляет следующий функционал:

- `/start`: Начать взаимодействие с ботом. Появляется клавиатура с двумя кнопками: "Трек" и "Статистика".

- "Трек": При выборе этой опции, бот извлекает данные из базы данных, которые нужно проверить, такие как название трека, исполнитель и айди на видео. Бот отправляет сообщение с этими данными и прикрепляет четыре инлайн кнопки: "Верно", "Изменить исполнителя", "Изменить название" и "Удалить".

- "Верно": При нажатии этой кнопки, данные записываются в другую таблицу с очищенными данными.

- "Изменить исполнителя" и "Изменить название": Предоставляют возможность изменить соответственно исполнителя или название трека.

- "Удалить": При нажатии этой кнопки данные не записываются в другую таблицу и помечаются как проверенные.

- "Статистика" (функционал в будущем): Запланированная функция для просмотра статистики данных.

## Инструкции по развертыванию и использованию

1. Установите Poetry

Если у вас еще нет Poetry, установите его с помощью следующих команд:

**Linux/macOS:**

   ```shell
curl -sSL https://install.python-poetry.org | python3 -
   ```

**Windows:**

Используйте официальный инсталлятор, который можно скачать [здесь](https://python-poetry.org/docs/#installing-with-the-official-installer).

   ```shell
   pip install -r requirements.txt
   ```

2. Установите зависимости с Poetry

Используйте Poetry для установки всех необходимых зависимостей:

   ```shell
   poetry install
   ```

3. Используйте базу данных с двумя таблицами для работы бота. Пример SQL-запросов для создания таблиц:

```sql
CREATE TABLE videos_untrusted (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    artist VARCHAR(255),
    video_id VARCHAR(255),
    time_listen TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    checked BOOLEAN DEFAULT false
);

CREATE TABLE videos (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    artist VARCHAR(255),
    video_id VARCHAR(255),
    time_checked TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```
4. Создайте .env файл

Скопируйте файл env.sample и переименуйте его в .env. Внутри этого файла заполните переменные окружения.

5. Запустите бота, используя:

 ```shell
python main.py
```

6. Введите `/start` в чате с ботом и начните использовать функционал.

## Пример использования

https://github.com/xxspell/validator-tg-bot/assets/74972395/ebff408c-28ff-450f-8d8c-17f8d1a9c2d9


## Развитие проекта

Планируется добавление дополнительных функций и улучшение бота. Если у вас есть предложения или проблемы, пожалуйста, [создайте issue](https://github.com/xxspell/validator-tg-bot/issues).

## Лицензия

Этот проект лицензируется в соответствии с [Лицензией MIT](LICENSE).
