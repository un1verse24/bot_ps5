from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb = ReplyKeyboardMarkup(resize_keyboard=True)
b1 = KeyboardButton('/start')
b2 = KeyboardButton('/search')
b3 = KeyboardButton('/smart')
b4 = KeyboardButton('/radar')
b5 = KeyboardButton('/radar_iphone')
kb.add(b1).add(b2).add(b3).add(b4).add(b5)

