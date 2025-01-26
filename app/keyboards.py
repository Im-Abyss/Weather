from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

change_city = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Другой город", 
                              callback_data='change_city')]]
)