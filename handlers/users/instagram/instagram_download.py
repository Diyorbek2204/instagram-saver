from aiogram import types
from aiogram.dispatcher.filters import Text
from handlers.users.instagram.instagram_send import instagram_download
from loader import dp


@dp.message_handler(Text(startswith="https://www.instagram.com/"))
async def insta(message: types.Message):
    link = message.text
    url = instagram_download(link=link)
    if url == "Bad":
        await message.answer("Wrong Input!")
    else:
        if url['type'] == 'image':
            await message.answer_photo(photo=url['media'])
        elif url['type'] == 'video':
            await message.answer_video(video=url['media'])
        elif url['type'] == 'carousel':
            for i in url['media']:
                await message.answer_document(document=i)
        else:
            await message.answer("Nothing in this URL!")