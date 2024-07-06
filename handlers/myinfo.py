from aiogram.filters.command import Command
from aiogram import types, Router

myinfo_router = Router()


@myinfo_router.message(Command('myinfo'))
async def info_handler(message: types.Message):
    print(message.from_user)
    await message.answer(f'Ваш id: {message.from_user.id}'
                         f'\nВаше имя: {message.from_user.first_name}'
                         f'\nВаш ник: {message.from_user.username}')
