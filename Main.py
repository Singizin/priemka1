import telebot
from telebot.types import Message
from telebot import types
from telebot import apihelper
from check import answer as a
from check import now

fma1 = 'https://www.nstu.ru/enrollee/entrance/entrance_list?competition=4397'  # Энергетика
fen1 = 'https://www.nstu.ru/enrollee/entrance/entrance_list?competition=4414'  # Энергетика
fma3 = 'https://www.nstu.ru/enrollee/entrance/entrance_list?competition=4399'  # Автоматизация

TOKEN = '854025714:AAH9Wi3_rWfVJvjnbDgNWkL8hYCbH2Fr-wY'
bot = telebot.TeleBot(TOKEN)
print('lololo')
bot.send_message(260119686, "Go")


@bot.message_handler(commands=['fen'])
def command_handler(message: Message):
    count, spisok = a(2)
    bot.send_message(message.from_user.id, count)
    bot.send_message(message.from_user.id, spisok)


@bot.message_handler(commands=['check'])
def start(m):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add('Направления', 'Прайс-лист')
    keyboard.add('Акции', 'Контакты')
    msg = bot.send_message(m.chat.id, 'Выберите функцию',
                           reply_markup=keyboard)
    bot.register_next_step_handler(msg, name)


def name(m):
    if m.text == 'Направления':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add('13.03.02')
        keyboard.add('15.03.04')
        msg = bot.send_message(m.chat.id, 'Выберите направление',
                               reply_markup=keyboard)
        bot.register_next_step_handler(msg, spisok)


def spisok(m):
    print(m.text)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add('копии', 'оригиналы')
    keyboard.add('контракт', 'ориг+согсасие')
    if m.text == '13.03.02':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add('копии', 'оригиналы')
        keyboard.add('контракт', 'ориг+согсасие')
        msg = bot.send_message(m.chat.id, 'какой список?', reply_markup=keyboard)
        bot.register_next_step_handler(msg, zapros)


# def zapros(m):
#     if m.text == 'копии':
#         bot.send_message(m.chat.id, now(url))
#     elif m.text == 'оригиналы':
#         bot.send_message(m.chat.id, now(url + '&o_only=1'))
#     # bot.send_message(call.from_user.id, now(fma3))


'''
@bot.message_handler(content_types=['text'])
@bot.edited_message_handler(content_types=['text'])
def echo_digits(message: Message):
    old = list(message.text.split(', '))
    otvet = a(1, fma1, old)
    print(otvet)
    bot.send_message(260119686, "{}".format(otvet))
'''

# bot.enable_save_reply_handlers(delay=1)


bot.polling(timeout=60)