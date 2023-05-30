from aiogram import types
from handlers.users.instagram.instagram_download import insta
from handlers.users.tiktok.tiktok_download import tik
from handlers.users.youtube.youtube_download import you
from loader import dp


@dp.callback_query_handler()
async def option(callback: types.CallbackQuery):
    if callback.data == "instagram":
        await callback.message.answer("Instagram... Input the URL!")

        return insta
    elif callback.data == "youtube":
        await callback.message.answer("YouTube... Input the URL!")

        return you
    elif callback.data == "tiktok":
        await callback.message.answer("TikTok... Input the URL!")

        return tik