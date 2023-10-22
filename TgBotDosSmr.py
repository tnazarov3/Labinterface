"""
import telebot
from telebot import types
from telebot.types import KeyboardButton, ReplyKeyboardMarkup, WebAppInfo

#bot = telebot.TeleBot('6362714649:AAEOjpU0NL6pu_DypST1JLIybi9U_WvxVMM')

web_app = WebAppInfo(url="https://tnazarov3.github.io/LabInterface")
@bot.message_handler(commands=['start'])
async def start(message: types.Message):
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton('Открыть', web_app = web_app)
    await message.answer('l', reply_markup=markup)
#keyboard = ReplyKeyboardMarkup(
    #keyboard=[
        #[KeyboardButton(text="Достопримечательности Самары", web_app=web_app)]
    #],
    #resize_keyboard=True
#)

DISC = {
    "1": "Благоприятными для Овнов в этот день будут физические",
    "2": "В этот день новые действия и мысли по отношению к"
}


@bot.message_handler(content_types='web_app_data')
def buy_process(web_app_message):
    bot.send_message(web_app_message.chat.id, DISC[f'{web_app_message.web_app_data}'])

#bot.polling(none_stop=True, interval=0)
    
"""
