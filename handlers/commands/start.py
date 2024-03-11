from loader import dp, db
from aiogram.dispatcher import FSMContext
from aiogram import types


@dp.message_handler(commands = 'start', state = "*")
async def start_command_handler(update : types.Message, state : FSMContext):
    if db.is_user(update.from_user.id):
        await update.answer("You are user")
        
    else:
        await update.answer(f"Assalomu alykum {update.from_user.first_name} men @ramazon2024_robot man. Men sizga iftorlik va saharlik vaxtlarni aytib bera olaman")
        db.registir(id = update.from_user.id, name = update.from_user.first_name)
        