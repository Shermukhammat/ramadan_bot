from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup





class InlineButtons:
    def __init__(self):
        self.cites = ['Andijon', 'Bekobod', 'Buxoro', 'Denov', 'Farg‘ona', 'Guliston', 'Jizzax', 'Kattako‘rg‘on', 'Namangan', 'Navoiy', 'Nukus', 'Nurota', 'Qarshi', 'Qo‘qon', 'Samarqand', 'Shahrisabz', 'Termiz', 'Toshkent', 'Urganch']

    def city_buttons(self):
        buttons = Buttons()
        for city in self.cites:
            buttons.add_button(InlineKeyboardButton(text = f"🏙 {city}", callback_data = city))

        buttons.add_button(InlineKeyboardButton(text = "⬅️ Orqaga", callback_data = 'back_menu'), new_line = True)
        return InlineKeyboardMarkup(inline_keyboard = buttons.get_buttons())


class Buttons:
    def __init__(self):
        self.buttons = [[]]
        self.index = 0
        self.curent_item_count = 0
    
    
    def add_button(self, button : InlineKeyboardButton, new_line : bool = False):
        if new_line:
            self.index += 1
            self.curent_item_count = 1
                
            self.buttons.append([])
            self.buttons[self.index].append(button)
            
        else:
            if self.curent_item_count < 3:
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