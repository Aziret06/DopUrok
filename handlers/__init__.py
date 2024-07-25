from aiogram import Router, F

from .menu import menu_router
from .start import start_router
from .review_dialog import review_dialog_router
from .dishes import dishes_router
from .myinfo import myinfo_router
from .random_recipe import random_recipe_router
from .group_activities import group_router
from .house_kg_parser import house_router

private_router = Router()

private_router.include_router(start_router)
private_router.include_router(myinfo_router)
private_router.include_router(house_router)
private_router.include_router(random_recipe_router)
private_router.include_router(dishes_router)
private_router.include_router(review_dialog_router)
private_router.include_router(menu_router)

private_router.message.filter(F.chat.type == 'private')
