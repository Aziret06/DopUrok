import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from dotenv import load_dotenv
from os import getenv
import logging
from random import choice

load_dotenv()
bot = Bot(token=getenv('MY_TOKEN'))
dp = Dispatcher()

recipe1 = ('Овсянка с ягодами:'
           '\nВ миске смешайте овсяные хлопья с молоком.'
           '\nДобавьте свежие ягоды (клубнику, малину или чернику).'
           '\nПосыпьте медом или корицей.')

recipe2 = ('Салат “Греческий”:'
           '\nНарежьте помидоры, огурцы, красный лук и оливки.'
           '\nДобавьте кубики феты.'
           '\nПолейте оливковым маслом и посыпьте солью и перцем.')

recipe3 = ('Тосты с авокадо:'
           '\nРазмягчите авокадо вилкой.'
           '\nНамажьте на гренки или тосты.'
           '\nПосыпьте солью, перцем и лимонным соком.')

recipe4 = ('Суп-пюре из тыквы:'
           '\nПриготовьте тыквенное пюре (тыкву отварите и разомните).'
           '\nДобавьте сливки и соль.'
           '\nПодавайте горячим.')

recipe5 = ('Банановые панкейки:'
           '\nВзбейте яйцо с молоком.'
           '\nДобавьте муку и разрыхлитель теста.'
           '\nЖарьте блинчики с нарезанными бананами.')

recipes = [recipe1, recipe2, recipe3, recipe4, recipe5]


@dp.message(Command('start'))
async def start_handler(message):
    print(message.from_user)
    await message.answer(f'Привет, {message.from_user.first_name}')


@dp.message(Command('myinfo'))
async def info_handler(message):
    print(message.from_user)
    await message.answer(f'Ваш id: {message.from_user.id}'
                         f'\nВаше имя: {message.from_user.first_name}'
                         f'\nВаш ник: {message.from_user.username}')


@dp.message(Command('random_recipe'))
async def recipe_handler(message):
    print(message.from_user)
    random_recipe = choice(recipes)
    await message.answer(random_recipe)


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
