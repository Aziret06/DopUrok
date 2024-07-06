from aiogram import types, Router, F

dishes_router = Router()


@dishes_router.message(F.text == 'холодные напитки')
async def dishes_handler(message: types.Message):
    image = types.FSInputFile('images/коктейль_дыня-мята.jpg')
    await message.answer_photo(
        photo=image,
        caption='Коктейль "Дыня с мятой"'
    )
    image = types.FSInputFile('images/коктейль_киви-яблоко.jpg')
    await message.answer_photo(
        photo=image,
        caption='Коктейль "Киви с яблоком"'
    )
    image = types.FSInputFile('images/коктейль_мохито.jpg')
    await message.answer_photo(
        photo=image,
        caption='Коктейль "Мохито"'
    )
    image = types.FSInputFile('images/коктейль_ягодно-фруктовый_микс.jpg')
    await message.answer_photo(
        photo=image,
        caption='Коктейль "Ягодно-фруктовый микс"'
    )


@dishes_router.message(F.text == 'горячие напитки')
async def dishes_handler(message: types.Message):
    image = types.FSInputFile('images/чай_с_травами.jpg')
    await message.answer_photo(
        photo=image,
        caption='Чай "Травяной"'
    )
    image = types.FSInputFile('images/чай_с_лимоном.jpg')
    await message.answer_photo(
        photo=image,
        caption='Чай "Лимонный"'
    )
    image = types.FSInputFile('images/чай_клубника-малина.jpg')
    await message.answer_photo(
        photo=image,
        caption='Чай "Клубнично-малиновый"'
    )
    image = types.FSInputFile('images/горячий_шоколад.jpg')
    await message.answer_photo(
        photo=image,
        caption='Горячий шоколад'
    )
