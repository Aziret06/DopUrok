from aiogram import Bot, Dispatcher, types
from dotenv import load_dotenv
from os import getenv
from database.database import Database

load_dotenv()
database = Database('db.sqlite3')
debug = getenv('DEBUG', 0)
if not debug:
    print('Бот запускается на сервере')
    from aiogram.client.session.aiohttp import AiohttpSession
    session = AiohttpSession(proxy=getenv('PROXY'))
    bot = Bot(token=getenv('MY_TOKEN'), session=session)
else:
    print('Бот запущен на компьютере')
    bot = Bot(token=getenv('MY_TOKEN'))
media = getenv('media')
dp = Dispatcher()
