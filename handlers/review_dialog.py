from aiogram import Router, types, F
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

from bot_config import bot, database

review_dialog_router = Router()


class RestaurantReview(StatesGroup):
    name = State()
    phone_number = State()
    visit_date = State()
    food_rating = State()
    cleanliness_rating = State()
    extra_comments = State()


@review_dialog_router.callback_query(F.data == 'feedback')
async def feedback_handler(callback: types.CallbackQuery, state: FSMContext):
    await state.set_state(RestaurantReview.name)
    await callback.answer()
    await bot.send_message(callback.from_user.id, text='Как вас зовут?')


@review_dialog_router.message(RestaurantReview.name)
async def process_name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(RestaurantReview.phone_number)
    await message.answer('Ваш номер телефона')


@review_dialog_router.message(RestaurantReview.phone_number)
async def process_phone_number(message: types.Message, state: FSMContext):
    phone_number = message.text

    if not phone_number.isdigit():
        await message.answer('Вводите только числа!')
        return

    await state.update_data(phone_number=message.text)
    await state.set_state(RestaurantReview.visit_date)
    await message.answer('Дата вашего визита (ДД-ММ-ГГГГ)')


@review_dialog_router.message(RestaurantReview.visit_date)
async def process_visit_date(message: types.Message, state: FSMContext):

    kb = types.ReplyKeyboardMarkup(
        keyboard=[
            [
                types.KeyboardButton(text='Замечательно', request=5)
            ],
            [
                types.KeyboardButton(text='Хорошо', request=4)
            ],
            [
                types.KeyboardButton(text='Удовлетворительно', request=3)
            ],
            [
                types.KeyboardButton(text='Так себе', request=2)
            ],
            [
                types.KeyboardButton(text='Отвратительно', request=1)
            ]
        ],
        resize_keyboard=True
    )

    await state.update_data(visit_date=message.text)
    await state.set_state(RestaurantReview.food_rating)
    await message.answer('Оцените качество еды', reply_markup=kb)


@review_dialog_router.message(RestaurantReview.food_rating)
async def process_food_rating(message: types.Message, state: FSMContext):

    ratings = {'Замечательно': 5, 'Хорошо': 4, 'Удовлетворительно': 3, 'Так себе': 2, 'Отвратительно': 1}
    
    kb = types.ReplyKeyboardRemove()
    try:
        await state.update_data(food_rating=ratings[message.text])
        await state.set_state(RestaurantReview.cleanliness_rating)
        await message.answer('Оцените чистоту ресторана (от 1 до 10)', reply_markup=kb)
    except KeyError:
        await message.answer('pres only buttons!!')
        await state.set_state(RestaurantReview.food_rating)


@review_dialog_router.message(RestaurantReview.cleanliness_rating)
async def process_cleanliness_rating(message: types.Message, state: FSMContext):
    cleanliness_rating = message.text
    if not cleanliness_rating.isdigit():
        await message.answer('Вводите только числа!')
        return

    cleanliness_rating = int(cleanliness_rating)
    if cleanliness_rating < 1 or cleanliness_rating > 10:
        await message.answer('От 1 до 10!')
        return

    await state.update_data(cleanliness_rating=message.text)
    await state.set_state(RestaurantReview.extra_comments)
    await message.answer('Дополнительный комментарий')


@review_dialog_router.message(RestaurantReview.extra_comments)
async def process_extra_comments(message: types.Message, state: FSMContext):
    await state.update_data(extra_comments=message.text)
    data = await state.get_data()
    database.execute('''
                INSERT INTO review_results (name, phone_number, visit_date, food_rating, cleanliness_rating, extra_comments)
                VALUES (?, ?, ?, ?, ?, ?)
    ''', (data['name'], data['phone_number'], data['visit_date'], data['food_rating'], data['cleanliness_rating'],
          data['extra_comments']))
    await state.clear()
    await message.answer('Спасибо за ваш отзыв!')
