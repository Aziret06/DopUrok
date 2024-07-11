from aiogram.filters.command import Command
from aiogram import types, Router
from random import choice
import os
from bot_config import media, bot
from aiogram.types import FSInputFile

random_recipe_router = Router()

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

recipes = [recipe5, recipe1, recipe2, recipe4, recipe3]


@random_recipe_router.message(Command('random_recipe'))
async def recipe_handler(message: types.Message):
    files = os.listdir(media + 'for_recipe')
    random_recipe = choice(recipes)
    ind = recipes.index(random_recipe)
    path = media + 'for_recipe/' + files[ind]
    print(path)
    photo = FSInputFile(path)
    await bot.send_photo(
        chat_id=message.from_user.id,
        photo=photo,
        caption=f'{random_recipe}'
    )
