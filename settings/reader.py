from dotenv import load_dotenv
import os
import logging

ascii_art = """
 ██▒   █▓ ▄▄▄       ██▓   ▓██   ██▓▓██   ██▓
▓██░   █▒▒████▄    ▓██▒    ▒██  ██▒ ▒██  ██▒
 ▓██  █▒░▒██  ▀█▄  ▒██░     ▒██ ██░  ▒██ ██░
  ▒██ █░░░██▄▄▄▄██ ▒██░     ░ ▐██▓░  ░ ▐██▓░
   ▒▀█░   ▓█   ▓██▒░██████▒ ░ ██▒▓░  ░ ██▒▓░
   ░ ▐░   ▒▒   ▓▒█░░ ▒░▓  ░  ██▒▒▒    ██▒▒▒ 
   ░ ░░    ▒   ▒▒ ░░ ░ ▒  ░▓██ ░▒░  ▓██ ░▒░ 
     ░░    ░   ▒     ░ ░   ▒ ▒ ░░   ▒ ▒ ░░  
      ░        ░  ░    ░  ░░ ░      ░ ░     
     ░                     ░ ░      ░ ░     
"""
print(ascii_art)
print('A bot for validating music data and uploading it to a database\nby xxspell')
load_dotenv()


def ex(key):
    return os.getenv(key)


log_level = logging.INFO
log_format = '%(asctime)s - %(name)s - %(levelname)s - %(module)s:%(funcName)s:%(lineno)d - %(message)s'

logging.basicConfig(level=log_level,
                    # Режим записи (перезапись файла)
                    format=log_format,
                    encoding='utf-8',
                    handlers=[logging.StreamHandler()])


bot_token = ex('BOT_TOKEN')
sql_host = ex('SQL_HOST')
sql_user = ex('SQL_USER')
sql_password = ex('SQL_PASSWORD')
sql_database = ex('SQL_DATABASE')
admin_id = ex('ADMIN_ID')


logging.info('Config loaded')
# print(sql_host)
# print(sql_user)
# print(sql_password)
# print(sql_database)
