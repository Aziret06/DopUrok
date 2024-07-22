from aiogram import Router, F, types
from aiogram.filters.command import Command

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


CATEGORIES = ('завтраки', 'восточные блюда', 'первые блюда')


@menu_router.message(F.text.lower().in_(CATEGORIES))
async def categories_handler(message: types.Message):
    kb = types.ReplyKeyboardRemove()
    sqlquery = '''
            SELECT dishes.*, dishes_category.name FROM 
            dishes JOIN dishes_category ON dishes_category.id=dishes.category_id
            WHERE dishes_category.name = ?
            '''
    category = message.text.lower()
    print('Category   ', category)

    dishes = database.fetch(
        query=sqlquery,
        params=(category,)
    )
    print(dishes)
    if not dishes:
        await message.answer('К сожвлению нет блюд в этой категории')
    await message.answer('Блюда категории "Завтраки"', reply_markup=kb)
    for dish in dishes:
        photo = types.FSInputFile(dish.get('cover'))
        await message.answer_photo(
            caption=f'Название: "{dish.get("name")}" '
                    f'\nЦена: {dish.get("price")}',
            photo=photo
        )
