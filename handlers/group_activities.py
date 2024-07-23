from aiogram import Router, types
from aiogram.filters.command import Command

from datetime import timedelta

from bot_config import bot

group_router = Router()

BAD_WORDS = ('терроризм', 'прощай', 'ботан', 'чудик')


@group_router.message()
async def echo(message: types.Message):
    for word in message.text.split():
        if word in BAD_WORDS:
            await message.delete()
            await message.answer(
                f'{message.from_user.first_name}, эти слова нельзя произносить!'
            )
            author = message.from_user.id
            await bot.ban_chat_member(
                chat_id=message.chat.id,
                user_id=author,
                until_date=timedelta(hours=2)
            )
