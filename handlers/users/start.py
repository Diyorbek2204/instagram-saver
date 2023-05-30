from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.inline.inline_buttons import inline_button_option
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Hello, {message.from_user.full_name}! This Bot can download Medias from Social Medias like Instagram, YouTube or TikTok! Choose options below👇🏾",
                         reply_markup=inline_button_option())