from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def inline_button_option():
    ikm_option = InlineKeyboardMarkup()

    button_option = InlineKeyboardButton(text="🟣Instagram", callback_data="instagram")

    ikm_option.add(button_option)

    return ikm_option