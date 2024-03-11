from aiogram import Bot
from config import BOT_TOKEN, DATA_CHANEL
import asyncio
import pandas as pd



data = pd.read_csv("scraping/ramadan.csv")
bot = Bot(BOT_TOKEN)




async def main():
    for index in data.index:
        try:
            row = data.iloc[index, :]

            message_data = await bot.send_photo(chat_id = "@youtuba_data", photo = open(f'scraping/images/{index}.png', 'rb'))   
            data.iloc[index, -1] = message_data.message_id
            print(message_data.message_id)
            
            await asyncio.sleep(5)
        
        except:
            print("ERROR")
        
        
    

asyncio.run(main())
data.to_csv("scraping/new.csv")

