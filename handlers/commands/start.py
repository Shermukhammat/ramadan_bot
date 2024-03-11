from loader import dp, db, keyboard, bot
from aiogram.dispatcher import FSMContext
from aiogram import types


@dp.message_handler(commands = 'start', state = "*")
async def start_command_handler(update : types.Message, state : FSMContext):
    # commands = [
    #         types.BotCommand(command = 'start', description = "Botni ishga tushrish"),
    #         types.BotCommand(command = 'info', description = "Bot haqida malumot")
    #     ]
    # await bot.set_my_commands(commands=commands)
    if db.is_user(update.from_user.id):
        await update.answer(f"{update.from_user.first_name} xush kelibsiz! Sizni yana ko'rib turganimdan xursandman!",
                            reply_markup = keyboard.main_menu())
        
    else:
        
        await update.answer(f"Assalomu alykum {update.from_user.first_name} men @ramazon2024_robot man. Men sizga iftorlik va saharlik vaxtlarni aytib bera olaman!",
                            reply_markup = keyboard.main_menu())
        db.registir(id = update.from_user.id, name = update.from_user.first_name)
        