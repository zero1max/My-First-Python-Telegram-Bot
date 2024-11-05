from telegram import InlineKeyboardMarkup, InlineKeyboardButton

inline_keyboard = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton("Start", callback_data="start"), InlineKeyboardButton("Help", callback_data="help")]
    ]
    )

back = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton("Back", callback_data='back')]
    ]
)