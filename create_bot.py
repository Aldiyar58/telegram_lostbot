from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()

bot = Bot('5610542782:AAF8_af_Y_oR0BIVoVQj6sHPTKLXclVaz0I')
dp = Dispatcher(bot, storage=storage)