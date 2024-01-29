from core.handlers.callbacks import *
from database.db import Db
from aiogram.types import CallbackQuery, FSInputFile, InputMediaPhoto, Message


async def get_start(message: Message, bot: Bot):
    await message.answer(f'Добро пожаловать в наш магазин, {message.from_user.first_name}!',
                         reply_markup=go_to_menu_inline_keyboard)
    db = Db()
    await db.save_user(message.from_user.id, message.from_user.username, message.from_user.first_name,
                       message.from_user.last_name)
