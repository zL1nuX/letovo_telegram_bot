# -*- coding: utf-8 -*-

import telebot
from telebot import types
from questions import keyboard as list_of_questions
from answers import answer_data
from Lingv import format_message
from responses import find_response

token = "your token"
bot = telebot.TeleBot(token)


def back_to_menu(message):
    keyboard = types.InlineKeyboardMarkup()
    key_FAQ = types.InlineKeyboardButton(text='FAQ', callback_data='FAQ')
    keyboard.add(key_FAQ)
    key_free = types.InlineKeyboardButton(text='Задать самому', callback_data='free')
    keyboard.add(key_free)
    question = 'Как я могу тебе помочь?'
    return question, keyboard


@bot.message_handler(func=lambda m: True)
def get_text_messages(message):
    if message.text == "/start":
        bot.send_message(message.from_user.id, "Привет! Напиши /que, чтобы начать.")
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши /start")

    elif message.text == "/que":
        bot.send_message(message.from_user.id, text=back_to_menu(message)[0], reply_markup=back_to_menu(message)[1])

    else:
        text_tokens = format_message(message.text)
        ans = find_response(text_tokens)
        if ans:
            bot.send_message(message.from_user.id, ans)
        else:
            bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /start, чтобы начать.")


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    print(call.data)
    if call.data == 'FAQ':
        # bot.send_message(call.message.chat.id, 'Ваш выбор - Принять')
        # bot.edit_message_text('Ваш выбор - FAQ', call.message.chat.id, call.message.message_id)
        bot.edit_message_text(
            'Выберите номер вопроса, который Вам интересен:\n 1. Как попасть в «Летово»? \n 2. Сколько стоит '
            'обучение? \n 3. Как определяется размер стипендии? \n 4. Как школьник может подготовиться к поступлению '
            'в «Летово»? \n 5. Есть ли какие-то ограничения при поступлении в школу «Летово», кроме возрастных? \n 6. '
            'По каким причинам заявка на поступление может быть отклонена? \n 7. Учитываются ли при поступлении '
            'внеучебные достижения? \n 8. Можно поступить в «Летово» в начальную школу, 5,6 классы? \n 9. Можно '
            'поступить в «Летово» в 10 и 11 классы? \n 10. Чем школа «Летово» отличается от обычной государственной '
            'школы? \n 11. Сколько учеников будет в каждом классе? \n 12. Как я могу познакомиться с учителями '
            '«Летово» до поступления? \n 13. Какие у вас будут профили обучения? \n 14. Насколько тяжело учиться в '
            '«Летово»? \n 15. Насколько просто изменить выбор предметов для углубленного изучения? \n 16. В школе '
            'можно будет проводить настоящие научные исследования и эксперименты? \n 17. Будут ли работать программы '
            'обмена с другими школами? \n 18. Чем проживающие в пансионе ученики занимаются на выходных? \n 19. '
            'Открыта ли школа на каникулах и праздниках? \n 20. Как школьники будут добираться до школы и обратно? \n '
            '21. Можно ли посетить кампус до поступления? \n 22. Как родители могут поучаствовать в жизни школы? \n '
            '23. Как я могу узнать о школе «Летово» ещё больше? \n 24. Какими документами и стандартами регулируется '
            'работа школы «Летово»?',
            call.message.chat.id,
            call.message.message_id, reply_markup=list_of_questions)
    elif call.data == 'free':
        # bot.send_message(call.message.chat.id, 'Задайте свой вопрос')
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data="back"))
        bot.edit_message_text('Задайте свой вопрос', call.message.chat.id, call.message.message_id, reply_markup=keyboard)




    elif call.data == "back":
        bot.send_message(call.message.chat.id, text=back_to_menu(call.message)[0],
                         reply_markup=back_to_menu(call.message)[1])

    elif int(call.data) in range(1, 25):
        ans = answer_data(int(call.data))
        bot.send_message(call.message.chat.id, ans)


bot.polling(none_stop=True, interval=0)
