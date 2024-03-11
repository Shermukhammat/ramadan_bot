from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton



class Keyboard:
    def __init__(self):
        self.cites = ['Andijon', 'Bekobod', 'Buxoro', 'Denov', 'Farg‘ona', 'Guliston', 'Jizzax', 'Kattako‘rg‘on', 'Namangan', 'Navoiy', 'Nukus', 'Nurota', 'Qarshi', 'Qo‘qon', 'Samarqand', 'Shahrisabz', 'Termiz', 'Toshkent', 'Urganch']
    
    def main_menu(self):
        buttons = [[KeyboardButton(text = "⏳ Bugun"), KeyboardButton(text = "⌛️ Ertaga")],
                   [KeyboardButton(text = "🗓 To'liq taqvim"), KeyboardButton(text = "🤲 Duo")],
                   [KeyboardButton(text = "📍 Shaharni o'zgartirish")]]
        
        return ReplyKeyboardMarkup(keyboard = buttons, resize_keyboard = True)
    
    
    def city_buttons(self):
        buttons = Buttons(item_count = 2)
        for city in self.cites:
            buttons.add_button(KeyboardButton(text = city))

        buttons.add_button(KeyboardButton(text = "⬅️ Orqaga"), new_line = True)
        return ReplyKeyboardMarkup(keyboard = buttons.get_buttons(), resize_keyboard = True)


class Buttons:
    def __init__(self, item_count : int = 3):
        self.buttons = [[]]
        self.index = 0
        self.curent_item_count = 0
        self.item_count = item_count
    
    
    def add_button(self, button : InlineKeyboardButton, new_line : bool = False):
        if new_line:
            self.index += 1
            self.curent_item_count = 1
                
            self.buttons.append([])
            self.buttons[self.index].append(button)
            
        else:
            if self.curent_item_count < self.item_count:
                self.curent_item_count += 1
                self.buttons[self.index].append(button)
            else:
                self.index += 1
                self.curent_item_count = 1
                
                self.buttons.append([])
                self.buttons[self.index].append(button)
    
    def get_buttons(self):
        return self.buttons
    
    
    def reset(self):
        self.buttons = [[]]
        self.index = 0
        self.curent_item_count = 0