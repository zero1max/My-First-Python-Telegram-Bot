from telegram import InlineKeyboardMarkup, InlineKeyboardButton

inline_keyboard = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton("Boshlash", callback_data="start"), InlineKeyboardButton("Yordam", callback_data="help")]
    ]
    )

back = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton("Ortga", callback_data='back')]
    ]
)