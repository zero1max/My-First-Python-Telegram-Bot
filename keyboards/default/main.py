from telegram import ReplyKeyboardMarkup, KeyboardButton


main_keyboard = ReplyKeyboardMarkup(
    [[KeyboardButton('Start')],
     [KeyboardButton('Help')]],
    resize_keyboard=True 
)
