from telebot import types

keyboard = types.InlineKeyboardMarkup()
temp = []
for i in range(1, 25):
    temp.append(types.InlineKeyboardButton(text=i, callback_data=i))
    if i % 3 == 0:
        keyboard.add(*temp)
        temp = []

keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="back"))
