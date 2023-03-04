from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards import kb_lost_find, kb_kotigoria1, kb_kotigoria2
from aiogram.types import ReplyKeyboardRemove
from data_base import sqlite_db

async def command_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Привет я бот по потеряшкам\nи я помогу тебе найти вещь или хозяена этой веший \nздесь ты можеш выстовить обивление о пропажы или о нахождений или же пролистав католог найтий свою вешь ', reply_markup=kb_lost_find)
        # await bot.send_message(message.from_user.id, 'Введите школьную почту:')
    except:
        await message.reply('Общатся с ботом\nчерез ЛС: https://t.me/about_physic_bot')
# раздел Функцей вывода данных из баз данных
# ______________________________________________________________________________________________________________________
async def command_lost_box(message: types.Message):
    await bot.send_message(message.from_user.id, 'Вот вес Католог:', reply_markup=kb_lost_find)
    await bot.send_message(message.from_user.id, 'Раздел спортивных вещей:')
    await sqlite_db.sql_read_sport(message)
    await bot.send_message(message.from_user.id, 'Раздел школных вещей:')
    await sqlite_db.sql_read_school(message)
    await bot.send_message(message.from_user.id, 'Раздел Акссесуаров:')
    await sqlite_db.sql_read_decorations(message)
    await bot.send_message(message.from_user.id, 'Раздел гаджотов:')
    await sqlite_db.sql_read_technique(message)

async def command_lost_box_cloth(message: types.Message):
    await bot.send_message(message.from_user.id, 'Вот раздел: Спортивные принадлежности и одежда ', reply_markup=kb_lost_find)
    await sqlite_db.sql_read_sport(message)

async def command_lost_box_decor(message: types.Message):
    await bot.send_message(message.from_user.id, 'Вот раздел: Украшение И Акссесуары ', reply_markup=kb_lost_find)
    await sqlite_db.sql_read_decorations(message)

async def command_lost_box_tech(message: types.Message):
    await bot.send_message(message.from_user.id, 'Вот раздел: Гаджеты ', reply_markup=kb_lost_find)
    await sqlite_db.sql_read_technique(message)

async def command_lost_box_school(message: types.Message):
    await bot.send_message(message.from_user.id, 'Вот раздел: Школьные вещий  ', reply_markup=kb_lost_find)
    await sqlite_db.sql_read_school(message)
# ______________________________________________________________________________________________________________________
# async def command_chek_person(message: types.Message):
        # text1 = message.text
        # if '@' in text1:
            #a = text1.find('@')
            #text1 = text1[a+1:]
            #if text1 == "ptr.nis.edu.kz":
                #await bot.send_message(message.from_user.id, 'Проверка прошла успешно\nтеперь выбери действие ', reply_markup=kb_lost_find)
            #else:
                #await bot.send_message(message.from_user.id, 'не прошел')
        #else:
            #await bot.send_message(message.from_user.id, 'зто даже не емайл')

async def command_i_lost(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Выбери катигорию', reply_markup=kb_kotigoria1)
    except:
        await message.reply('Общаться с ботом\nчерез ЛС: https://t.me/about_physic_bot')

async def command_i_find(message : types.Message):
    try:
        await bot.send_message(message.from_user.id, "Выбери категорию этьой веший", reply_markup=kb_kotigoria2)
    except:
        await message.reply('Общаться с ботом\nчерез ЛС: https://t.me/about_physic_bot')

async def return_command(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, "Ok", reply_markup=kb_lost_find)
    except:
        await message.reply('Общаться с ботом\nчерез ЛС: https://t.me/about_physic_bot')

def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(command_i_lost, commands=['Я_потерял'])
    dp.register_message_handler(command_i_find,commands=['Я_нашел'])
    dp.register_message_handler(return_command, commands=['Назад'])
    dp.register_message_handler(command_lost_box, commands=['Вес_Католог'])
    dp.register_message_handler(command_lost_box_cloth, commands=['Раздел_спорта_и_одежды'])
    dp.register_message_handler(command_lost_box_decor, commands=['Украшение_И_Акссесуары'])
    dp.register_message_handler(command_lost_box_tech, commands=['Гаджеты'])
    dp.register_message_handler(command_lost_box_school, commands=['Школные_вещий'])

