from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb = ReplyKeyboardMarkup(resize_keyboard=True)
b1 = KeyboardButton('/start')
b2 = KeyboardButton('/search')
kb.add(b1).add(b2)

