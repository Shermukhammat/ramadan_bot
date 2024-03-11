from aiogram import Bot, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from config import BOT_TOKEN
from data import DataBase
from buttons import Keyboard, InlineButtons
from utilits import States


bot = Bot(BOT_TOKEN)
dp = Dispatcher(bot, storage = MemoryStorage())

db = DataBase()
states = States()

keyboard = Keyboard()
inline = InlineButtons()