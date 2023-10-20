import telebot
# from telebot import types
from telebot.types import KeyboardButton, ReplyKeyboardMarkup, WebAppInfo

global msg

bot = telebot.TeleBot('6362714649:AAEOjpU0NL6pu_DypST1JLIybi9U_WvxVMM')

web_app = WebAppInfo(url="https://tnazarov3.github.io/LabInterface")
keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Достопримечательности Самары", web_app=web_app)]
    ],
    resize_keyboard=True
)

DISC = {
    '1': 'Благоприятными для Овнов в этот день будут физические',
    '2': 'В этот день новые действия и мысли по отношению к'
}


@bot.message_handler(content_types='web_app_data')
async def buy_process(web_app_message):
    print(web_app_message) #вся информация о сообщении
    print(web_app_message.web_app_data.data)
    await bot.send_message(web_app_message.chat.id, DISC[f'{web_app_message.web_app_data}'])
