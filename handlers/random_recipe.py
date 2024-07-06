from aiogram.filters.command import Command
from aiogram import types, Router
from random import choice

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

recipes = [recipe1, recipe2, recipe3, recipe4, recipe5]


@random_recipe_router.message(Command('random_recipe'))
async def recipe_handler(message: types.Message):
    random_recipe = choice(recipes)
    await message.answer(random_recipe)
