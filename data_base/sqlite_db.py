import sqlite3 as sq
from create_bot import bot

def sql_start():
    global base, cur, announcement, cur_ann
    base = sq.connect('box.db')
    cur = base.cursor()
    announcement = sq.connect('Announcement.db')
    cur_ann = announcement.cursor()

    if base:
        print('Data base conected OK!')
    base.execute('CREATE TABLE IF NOT EXISTS menu(img TEXT,name TEXT, class TEXT, person TEXT)')
    base.execute('CREATE TABLE IF NOT EXISTS box_close(img TEXT,name TEXT, class TEXT, person TEXT)')
    base.execute('CREATE TABLE IF NOT EXISTS box_decor(img TEXT,name TEXT, class TEXT, person TEXT)')
    base.execute('CREATE TABLE IF NOT EXISTS box_tech(img TEXT,name TEXT, class TEXT, person TEXT)')
    base.execute('CREATE TABLE IF NOT EXISTS box_school(img TEXT,name TEXT, class TEXT, person TEXT)')
    base.commit()

# Раздел добовление данных
# ______________________________________________________________________________________________________________________

async def sql_add_command(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO menu VALUES (?,?,?,?)', tuple(data.values()))
        base.commit()

async def sql_base_close_command(state):
    async with state.proxy() as data:
        base.execute('INSERT INTO box_close VALUES (?,?,?,?)', tuple(data.values()))
        base.commit()

async def sql_base_decorations_command(state):
    async with state.proxy() as data:
        base.execute('INSERT INTO box_decor VALUES (?,?,?,?)', tuple(data.values()))
        base.commit()

async def sql_base_technique_command(state):
    async with state.proxy() as data:
        base.execute('INSERT INTO box_tech VALUES (?,?,?,?)', tuple(data.values()))
        base.commit()

async def sql_base_school_command(state):
    async with state.proxy() as data:
        base.execute('INSERT INTO box_school VALUES (?,?,?,?)', tuple(data.values()))
        base.commit()
# ______________________________________________________________________________________________________________________
# Раздел читение данных:
# ______________________________________________________________________________________________________________________

async def sql_read(message):
    for ret in cur.execute('SELECT * FROM menu').fetchall():
        await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\nОписание:  {ret[2]}\nФИО нашедшого: {ret[-1]}')

async def sql_read_sport(message):
    for ret in cur.execute('SELECT * FROM box_close').fetchall():
        await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\nОписание:  {ret[2]}\nФИО нашедшого: {ret[-1]}')

async def sql_read_decorations(message):
    for ret in cur.execute('SELECT * FROM box_decor').fetchall():
        await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\nОписание:  {ret[2]}\nФИО нашедшого: {ret[-1]}')

async def sql_read_technique(message):
    for ret in cur.execute('SELECT * FROM box_tech').fetchall():
        await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\nОписание:  {ret[2]}\nФИО нашедшого: {ret[-1]}')

async def sql_read_school(message):
    for ret in cur.execute('SELECT * FROM box_school').fetchall():
        await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\nкласс:  {ret[2]}\nФИО нашедшого: {ret[-1]}')
