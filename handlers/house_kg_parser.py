from aiogram import Router, types, F
from crawler.house_kg import HouseParser

house_router = Router()


@house_router.callback_query(F.data == 'houses')
async def show_houses_links(callback: types.CallbackQuery):
    await callback.answer()
    house_parser = HouseParser()
    house_parser.get_page()
    links = house_parser.get_flat_links()
    print(links)
    for link in links:
        await callback.message.answer(link)
