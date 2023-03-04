from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards import kb_lost_find, kb_kotigoria1, kb_stop, grade_button_kb
from aiogram.types import ReplyKeyboardRemove
from aiogram.dispatcher.filters import Text
from data_base import sqlite_db


class FSMA_close(StatesGroup):
    photo = State()
    name = State()
    grade = State()
    person = State()


async def acm_start(message: types.Message):
    await FSMA_close.photo.set()
    await message.reply('Загрузи фото потерянной вещи', reply_markup=kb_stop)


async def load_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[0].file_id
    await FSMA_close.next()
    await message.reply('теперь введи название предмета')


async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await FSMA_close.next()
    await message.reply('Теперь укажи свой класс', reply_markup=grade_button_kb)


async def load_grade(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['grade'] = message.text
    await FSMA_close.next()
    await message.reply('теперь укажи своё ФИ', reply_markup=kb_stop)



async def load_person(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['person'] = message.text

    с8 = ['Уалиев Алдияр','Хабдрахим Султан']
    if data['grade'] == 'c8' or data['grade'] == 'с8':
        if data['person'] in с8:
            await message.answer('Поверка прошла успешна')
            await sqlite_db.sql_base_close_command(state)
            await message.answer("данные занесены в Католог бота", reply_markup=kb_lost_find)
            await state.finish()
        else:
            await message.answer('Поверка прошла не успешна')

    else:
        print('error')

    # Выход из состояний
    # @dp.message_handler(state="*", commands='отмена')
    # @dp.message_handler(Text(equals='отмена', ignore_case=True), state="*")


async def cancel_handler(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.reply('Ok задача была отменена', reply_markup=kb_lost_find)


def register_handlers_unit(dp: Dispatcher):
    dp.register_message_handler(acm_start, commands=['Спортивные_принадлежности_и_одежда'], state=None)
    dp.register_message_handler(load_photo, content_types=['photo'], state=[FSMA_close.photo])
    dp.register_message_handler(load_name, state=FSMA_close.name)
    dp.register_message_handler(load_person, state=FSMA_close.person)
    dp.register_message_handler(load_grade, state=FSMA_close.grade)
    dp.register_message_handler(cancel_handler, state="*", commands='Отмена')
