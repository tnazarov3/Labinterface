import sqlite3
import telebot
from telebot import types

global msg

bot = telebot.TeleBot('6362714649:AAEOjpU0NL6pu_DypST1JLIybi9U_WvxVMM')
conn = sqlite3.connect("D:/Bases/chat_db.db", check_same_thread=False)
cur = conn.cursor()


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == '/start':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Парки')
        btn2 = types.KeyboardButton('Памятники')
        btn3 = types.KeyboardButton('Знаковые места')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.from_user.id, 'Выберите интересующую вас категорию достопримечательностей',
                         reply_markup=markup)

    elif message.text == 'Парки':
        keyboard = types.InlineKeyboardMarkup()
        key_park1 = types.InlineKeyboardButton(
            text=conn.execute("Select NAME from PARKS WHERE id == 1 ").fetchone()[0], callback_data='park1'
        )
        keyboard.add(key_park1)
        key_park2 = types.InlineKeyboardButton(
            text=conn.execute("Select NAME from PARKS WHERE id == 2 ").fetchone()[0], callback_data='park2'
        )
        keyboard.add(key_park2)

        bot.send_message(message.from_user.id, text='Какой парк вас вас интересует?', reply_markup=keyboard)

    elif message.text == 'Памятники':
        keyboard = types.InlineKeyboardMarkup()
        key_mon1 = types.InlineKeyboardButton(
            text=conn.execute("Select NAME from MONUMENTS WHERE id == 1 ").fetchone()[0], callback_data='monument1'
        )
        keyboard.add(key_mon1)
        key_mon2 = types.InlineKeyboardButton(
            text=conn.execute("Select NAME from MONUMENTS WHERE id == 2 ").fetchone()[0], callback_data='monument2'
        )
        keyboard.add(key_mon2)

        bot.send_message(message.from_user.id, text='Какой памятник вас вас интересует?', reply_markup=keyboard)

    elif message.text == 'Знаковые места':
        keyboard = types.InlineKeyboardMarkup()
        key_place1 = types.InlineKeyboardButton(
            text=conn.execute("Select NAME from PLACES WHERE id == 1 ").fetchone()[0], callback_data='place1'
        )
        keyboard.add(key_place1)
        key_place2 = types.InlineKeyboardButton(
            text=conn.execute("Select NAME from PLACES WHERE id == 2 ").fetchone()[0], callback_data='place2'
        )
        keyboard.add(key_place2)

        bot.send_message(message.from_user.id, text='Какое знаковое место вас вас интересует?', reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    global msg
    if call.data == "park1":
        x = conn.execute("Select LAT, LEN from PARKS WHERE id == 1 ").fetchone()
        bot.send_location(call.from_user.id, x[0], x[1])
        msg = conn.execute("Select DISC from PARKS WHERE id == 1 ").fetchone()[0]
    elif call.data == "park2":
        x = conn.execute("Select LAT, LEN from PARKS WHERE id == 2 ").fetchone()
        bot.send_location(call.from_user.id, x[0], x[1])
        msg = conn.execute("Select DISC from PARKS WHERE id == 2 ").fetchone()[0]
    elif call.data == "monument1":
        x = conn.execute("Select LAT, LEN from MONUMENTS WHERE id == 1 ").fetchone()
        bot.send_location(call.from_user.id, x[0], x[1])
        msg = conn.execute("Select DISC from MONUMENTS WHERE id == 1 ").fetchone()[0]
    elif call.data == "monument2":
        x = conn.execute("Select LAT, LEN from MONUMENTS WHERE id == 2 ").fetchone()
        bot.send_location(call.from_user.id, x[0], x[1])
        msg = conn.execute("Select DISC from MONUMENTS WHERE id == 2 ").fetchone()[0]
    elif call.data == "place1":
        x = conn.execute("Select LAT, LEN from PLACES WHERE id == 1 ").fetchone()
        bot.send_location(call.from_user.id, x[0], x[1])
        msg = conn.execute("Select DISC from PLACES WHERE id == 1 ").fetchone()[0]
    elif call.data == "place2":
        x = conn.execute("Select LAT, LEN from PLACES WHERE id == 2 ").fetchone()
        bot.send_location(call.from_user.id, x[0], x[1])
        msg = conn.execute("Select DISC from PLACES WHERE id == 2 ").fetchone()[0]
    bot.send_message(call.message.chat.id, msg)


bot.polling(none_stop=True, interval=0)
