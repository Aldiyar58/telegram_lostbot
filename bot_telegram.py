from aiogram.utils import executor
from create_bot import dp
from data_base import sqlite_db

async def on_startup(_):
    print('хозяин я здесь')
    sqlite_db.sql_start()

from handlers import client, admin, other, sport_close_db, sql_tehnolgi_db, sql_base_decorations, sql_base_school

sport_close_db.register_handlers_unit(dp)
sql_base_decorations.register_handlers_unit(dp)
sql_base_school.register_handlers_unit(dp)
sql_tehnolgi_db.register_handlers_unit(dp)
client.register_handlers_client(dp)
# admin.register_handlers_admin(dp)
# other.register_handlers_other(dp)







executor.start_polling(dp, skip_updates=True, on_startup=on_startup)