from aiogram.filters.command import Command
from aiogram import types, Router, F

start_router = Router()


@start_router.message(Command('start'))
async def start_handler(message: types.Message):
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text='О нас', callback_data='about_us'),
                types.InlineKeyboardButton(text='Наш инстаграм', url='https://instagram.com')
            ],
            [
                types.InlineKeyboardButton(text='Наш адрес', url='https://2gis.kg'),
                types.InlineKeyboardButton(text='Вакансии', callback_data='jobs')
            ]
        ]
    )
    await message.answer(f'Привет, {message.from_user.first_name}!', reply_markup=kb)


@start_router.callback_query(F.data == 'about_us')
async def about_us_handler(callback: types.CallbackQuery):
    await callback.answer()
    await callback.message.answer('Мы являемся одним из популярнейших ресторанов в Средней Азии. '
                                  'Наши блюда готовятся толко из экологически чистых продуктов.')


@start_router.callback_query(F.data == 'jobs')
async def about_us_handler(callback: types.CallbackQuery):
    await callback.answer()
    await callback.message.answer('Требуется повар со стажем работы не менее 3 лет.'
                                  '\nТребуются посудомойщики в возрасте от 18 лет.'
                                  '\nТребуются официанты, стаж необязателен, в возрасте от 18 лет.')
