from loader import dp, db, bot, keyboard, inline, states
from aiogram.dispatcher import FSMContext
from aiogram import types
from utilits import is_ramadan, get_now, convert_now_to_str, get_tmorow
from config import DATA_CHANEL

saharlik = "<b>Саҳарлик (оғиз ёпиш) дуоси:</b>\nНавайту ан асума совма шаҳри Рамазона минал фажри илал мағриби, холисан лиллаҳи таъала."
iftorlik = "<b>Ифторлик (оғиз очиш) дуоси:</b>\nАллоҳумма лака сумту ва бика аманту ва аъалайка таваккалту ва ъала ризқика афтарту, фағфирли, йа Ғоффару, ма қоддамту вама аххорту."
months = {3 : 'mart', 4 : 'aprel'}

@dp.message_handler()
async def main_message_handler(update : types.Message, state : FSMContext):
    if db.is_user(update.from_user.id):
        if update.text == "🤲 Duo":
            await bot.send_photo(chat_id = update.from_user.id, photo = open('data/images/ramadan_dua.png', 'rb'), 
                                 caption="{}\n \n{}".format(saharlik, iftorlik), 
                                 parse_mode='HTML',
                                 reply_markup = keyboard.main_menu())
        
        elif update.text == "📍 Shaharni o'zgartirish":
            await state.set_state(states.chose_region)
            await update.answer("Quydagi shaxarlardan birni tanlang 👇🏻", reply_markup = keyboard.city_buttons())
        
        elif update.text == "⏳ Bugun":
            region = db.users[update.from_user.id]['region']
            if region:
                now = get_now()
                if is_ramadan(now):
                    now_str = convert_now_to_str(now)
                    
                    data = db.get_ramadan_info(date = now_str, city = region)
                    if data:         
                        await bot.copy_message(chat_id = update.from_user.id,
                                               from_chat_id = DATA_CHANEL,
                                               message_id = data['data_id'],
                                               caption = f"🕌 Ramazon 2024 {data['day']}-kun \n📆 {now.day}-{months.get(now.month)} {data['week']} \n\n☀️ Saharlik : {data['start']}  \n🌙 Iftorlik : {data['end']}")
                    
                    # await update.answer(f"Now is ramadan")
                else:
                    await update.answer("ramadan alredy ended")
                
            else:
                await state.set_state(states.chose_region)
                await update.answer("Ilimos o'z shahringizni tanlang 👇🏻", reply_markup = keyboard.city_buttons())
        
        
        elif update.text == "⌛️ Ertaga":
            region = db.users[update.from_user.id]['region']
            if region:
                tmorow = get_tmorow()
                if is_ramadan(tmorow):
                    tmorow_str = convert_now_to_str(tmorow)
                    data = db.get_ramadan_info(date = tmorow_str, city = region)
                    if data:         
                        await bot.copy_message(chat_id = update.from_user.id,
                                               from_chat_id = DATA_CHANEL,
                                               message_id = data['data_id'],
                                               caption = f"🕌 Ramazon 2024 {data['day']}-kun \n📆 {tmorow.day}-{months.get(tmorow.month)} {data['week']} \n\n☀️ Saharlik : {data['start']}  \n🌙 Iftorlik : {data['end']}")
                    
                    # await update.answer(f"Now is ramadan")
                    else:
                        await update.answer("ramadan alredy ended")
                        
            else:
                await state.set_state(states.chose_region)
                await update.answer("Ilimos o'z shahringizni tanlang 👇🏻", reply_markup = keyboard.city_buttons())
            
        else:
            await update.answer("Quydagi tugmalrdan birni bosing", reply_markup = keyboard.main_menu())
    
    else:
        await update.answer(f"Assalomu alykum {update.from_user.first_name} men @ramazon2024_robot man. Men sizga iftorlik va saharlik vaxtlarni aytib bera olaman!",
                            reply_markup = keyboard.main_menu())
        db.registir(id = update.from_user.id, name = update.from_user.first_name)
        
        

@dp.message_handler(state = states.chose_region)
async def chose_region_handler(update : types.Message, state : FSMContext):
    if update.text == "⬅️ Orqaga":
        await state.finish()
        await update.answer("🎛 Bosh menu", reply_markup = keyboard.main_menu())
        
    elif update.text in keyboard.cites:
        await state.finish()
        await update.answer(f"✅ Siz {update.text} shahrini tanladingiz !", reply_markup = keyboard.main_menu())
        db.update_user_region(id = update.from_user.id, region = update.text)
        
    else:
        await update.answer("❌ Iltimos quydagi shaharlardan birni tanlang", reply_markup = keyboard.city_buttons())