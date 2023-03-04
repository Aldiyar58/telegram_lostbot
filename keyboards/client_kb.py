from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

b1 = KeyboardButton('/Я_нашел')
b2 = KeyboardButton('/Я_потерял')
b3 = KeyboardButton('/Я_ищу')

botton_cotoloc = KeyboardButton('/Вес_Католог')
button_kotigoria = KeyboardButton('/Спортивные_принадлежности_и_одежда')
button_kotigoria1 = KeyboardButton('/Техника')
button_kotigoria2 = KeyboardButton('/Школьные_вещи')
button_kotigoria3 = KeyboardButton('/Украшения')

button_razdel1 = KeyboardButton('/Раздел_спорта_и_одежды')
button_razdel2 = KeyboardButton('/Украшение_И_Акссесуары')
button_razdel3 = KeyboardButton('/Гаджеты')
button_razdel4 = KeyboardButton('/Школные_вещий')

grade_button = KeyboardButton('c8')

button_stop = KeyboardButton('/Отмена')

return_kb = KeyboardButton('/Назад')

kb_lost_find = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_kotigoria1 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_kotigoria2 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_stop = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
grade_button_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

kb_lost_find.add(b1).row(b2, b3)
kb_kotigoria1.add(botton_cotoloc).row(button_razdel1, button_razdel2).row(button_razdel3, button_razdel4).row(return_kb)
kb_kotigoria2.row(button_kotigoria, button_kotigoria1).row(button_kotigoria2, button_kotigoria3).row(return_kb)
grade_button_kb.add(grade_button), grade_button_kb.row(button_stop)

kb_stop.add(button_stop)