from aiogram import Router, F, types
from aiogram.filters.command import Command
import sqlite3

from bot_config import database

menu_router = Router()


@menu_router.message(Command('menu'))
async def show_menu(message: types.Message):
    kb = types.ReplyKeyboardMarkup(
        keyboard=[
            [
                types.KeyboardButton(text='Завтраки')
            ],
            [
                types.KeyboardButton(text='Восточные блюда')
            ],
            [
                types.KeyboardButton(text='Первые блюда')
            ]
        ],
        resize_keyboard=True
    )
    await message.answer(
        text='Выберите категорию блюд',
        reply_markup=kb
    )


@menu_router.message(F.text.lower() == 'завтраки')
async def lunch_handler(message: types.Message):
    kb = types.ReplyKeyboardRemove()
    sqlquery = '''
            SELECT dishes.*, dishes_category.name FROM 
            dishes JOIN dishes_category ON dishes_category.id=dishes.category_id
            WHERE dishes_category.name = ?
            '''
    category = 'Завтраки'

    dishes = database.fetch(
        query=sqlquery,
        params=(category,)
    )
    print(dishes)
    await message.answer('Блюда категории "Завтраки"', reply_markup=kb)
    for dish in dishes:
        await message.answer(f'Название: {dish[1]}, Цена: {dish[2]}')


@menu_router.message(F.text.lower() == 'восточные блюда')
async def east_dishes_handler(message: types.Message):
    kb = types.ReplyKeyboardRemove()
    sqlquery = '''
            SELECT dishes.*, dishes_category.name FROM 
            dishes JOIN dishes_category ON dishes_category.id=dishes.category_id
            WHERE dishes_category.name = ?
            '''
    category = 'Восточные блюда'

    dishes = database.fetch(
        query=sqlquery,
        params=(category,)
    )
    print(dishes)
    await message.answer('Блюда категории "Восточные блюда"', reply_markup=kb)
    for dish in dishes:
        await message.answer(f'Название: {dish[1]}, Цена: {dish[2]}')


@menu_router.message(F.text.lower() == 'первые блюда')
async def first_dishes_handler(message: types.Message):
    kb = types.ReplyKeyboardRemove()
    sqlquery = '''
            SELECT dishes.*, dishes_category.name FROM 
            dishes JOIN dishes_category ON dishes_category.id=dishes.category_id
            WHERE dishes_category.name = ?
            '''
    category = 'Первые блюда'

    dishes = database.fetch(
        query=sqlquery,
        params=(category,)
    )
    print(dishes)
    await message.answer('Блюда категории "Первые блюда"', reply_markup=kb)
    for dish in dishes:
        await message.answer(f'Название: {dish[1]}, Цена: {dish[2]}')
