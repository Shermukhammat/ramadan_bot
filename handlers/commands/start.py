from loader import dp
from aiogram.dispatcher import FSMContext
from aiogram import types


@dp.message_handler(commands = 'start', state = "*")
async def start_command_handler(update : types.Message, state : FSMContext):
    await update.answer("Assalom alykum")