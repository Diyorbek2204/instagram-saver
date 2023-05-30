from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def inline_button_option():
    ikm_option = InlineKeyboardMarkup()

    button_option = InlineKeyboardButton(text="🟣Instagram", callback_data="instagram")
    button_option2 = InlineKeyboardButton(text="🔴YouTube", callback_data="youtube")
    button_option3 = InlineKeyboardButton(text="⚫TikTok", callback_data="tiktok")

    ikm_option.add(button_option, button_option2, button_option3)

    return ikm_option