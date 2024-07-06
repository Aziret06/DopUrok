from aiogram import Bot, Dispatcher, types
from dotenv import load_dotenv
from os import getenv

load_dotenv()
bot = Bot(token=getenv('MY_TOKEN'))
dp = Dispatcher()
