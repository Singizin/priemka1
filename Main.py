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
bot.send_message(260119686, "Go")
global user
user = {}

keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard.add('/fen', '/check')


@bot.message_handler(commands=['fen'])
def command_handler(message: Message):
    count, spisok = a(2)
    bot.send_message(message.from_user.id, count)
    bot.send_message(message.from_user.id, spisok)


@bot.message_handler(commands=['check'])
def start(m):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add('Направления')
    keyboard.add('/fen', '/check')
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
    if m.text == '13.03.02':
        user.update({m.chat.id : '1'})
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add('копии', 'оригиналы')
        keyboard.add('контракт', 'ориг+согсасие')
        msg = bot.send_message(m.chat.id, 'какой список?', reply_markup=keyboard)
        bot.register_next_step_handler(msg, zapros)
    elif m.text == '15.03.04':
        user.update({m.chat.id : '2'})
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add('копии', 'оригиналы')
        keyboard.add('контракт', 'ориг+согсасие')
        msg = bot.send_message(m.chat.id, 'какой список?', reply_markup=keyboard)
        bot.register_next_step_handler(msg, zapros)


def zapros(m):
    if user.get(m.chat.id) == '1':
        url = fma1
        napr ='#энергетика'
    elif user.get(m.chat.id) == '2':
        url = fma3
        napr ='#автоматизация'
    if m.text == 'копии':
        bot.send_message(m.chat.id, "{}_копии, {}".format(napr, now(url)))
    elif m.text == 'оригиналы':
        bot.send_message(m.chat.id, "{}_оригиналы, {}".format(napr, now(url + '&o_only=1')))
    elif m.text == 'ориг+согласие':
        bot.send_message(m.chat.id, "{}_огириналы+согласие, {}".format(napr, now(url + '&o_only=2')))
    elif m.text == 'контракт':
        bot.send_message(m.chat.id, "{}_контракт, {}".format(napr, now(url + '&o_only=3')))
    user.update({m.chat.id:'0'})
    bot.send_message(m.chat.id, "/fen \n /check")
    return


@bot.message_handler(content_types=['text'])
@bot.edited_message_handler(content_types=['text'])
def echo_digits(message: Message):
    old = list(message.text.split(', '))
    first = old[0].split('_')
    if first[0] == '#энергетика':
        url = fma1
    elif first[0] == '#автоматизация':
        url = fma3
    if first[1] == 'копии':
        pass
    elif first[1] == 'оригиналы':
        url = url + '&o_only=1'
    elif first[1] == 'ориг+согласие':
        url = url + '&o_only=2'
    elif first[1] == 'контракт':
        url = url + '&o_only=3'

    otvet = a(1, url, old)
    msg = bot.send_message(message.chat.id, "{}".format(otvet), reply_markup=keyboard)
    bot.register_next_step_handler(msg, start)


# bot.enable_save_reply_handlers(delay=1)


bot.polling(timeout=60)
