from aiogram import Bot, Dispatcher, types
from dotenv import load_dotenv
from os import getenv
from database.database import Database

load_dotenv()
bot = Bot(token=getenv('MY_TOKEN'))
media = getenv('media')
dp = Dispatcher()
database = Database('db.sqlite3')
