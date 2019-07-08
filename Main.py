import telebot
from telebot.types import Message
from telebot import types
from telebot import apihelper
from check import answer as a
from check import now

fma1 = 'https://www.nstu.ru/enrollee/entrance/entrance_list?competition=4397'  # Энергетика
fen1 = 'https://www.nstu.ru/enrollee/entrance/entrance_list?competition=4414'  # Энергетика
fma3 = 'https://www.nstu.ru/enrollee/entrance/entrance_list?competition=4399'  # Автоматизация
proxy = '78.186.140.120:58177'
apihelper.proxy = {'https': 'https://{}'.format(proxy)}
# TOKEN = '747611758:AAEpFP3iLMCbtmrLF0omSyTnjP7d7CCIaPY'
TOKEN = '854025714:AAH9Wi3_rWfVJvjnbDgNWkL8hYCbH2Fr-wY'
bot = telebot.TeleBot(TOKEN)
i = 0
bot.send_message(260119686, "Go")

global user
user = {}
global what
what = {}

@bot.message_handler(commands=['fen'])
def command_handler(message: Message):
    count, spisok = a(2)
    bot.send_message(message.from_user.id, count)
    bot.send_message(message.from_user.id, spisok)


@bot.message_handler(commands=['check'])
def start(m):
    user.update({m.chat.id : '0'})
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add('Направления', 'Сравнить с')
    keyboard.add('/fen', '/check')
    msg = bot.send_message(m.chat.id, 'Выберите функцию',
                           reply_markup=keyboard)
    bot.register_next_step_handler(msg, name)


def name(m):
    if m.text == 'Направления':
        what.update({m.chat.id:1})
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add('13.03.02','15.03.04')
        keyboard.add('/check')
        msg = bot.send_message(m.chat.id, 'Выберите направление',
                               reply_markup=keyboard)
        bot.register_next_step_handler(msg, spisok)
    if m.text == 'Сравнить':
        what.update({m.chat.id: 1})
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add('13.03.02','15.03.04')
        keyboard.add('/check')
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


def zapros(m):
    msg = bot.send_message('Выберите список')
    if user.get(m.chat.id) == '1':
        url = fma1
    elif user.get(m.chat.id) == '2':
        url = fma3
    if m.text == 'копии':
        if what.get(m.chat.id) == 1:
            bot.send_message(m.chat.id, now(url))
    elif m.text == 'оригиналы':
        if what.get(m.chat.id) == 1:
            bot.send_message(m.chat.id, now(url + '&o_only=1'))
    elif m.text == 'ориг+согласие':
        if what.get(m.chat.id) == 1:
            bot.send_message(m.chat.id, now(url + '&o_only=2'))
    elif m.text == 'контракт':
        if what.get(m.chat.id) == 1:
            bot.send_message(m.chat.id, now(url + '&o_only=3'))
    if what.get(m.chat.id) == 2:
        bot.register_next_step_handler(msg, compare)


def compare(m):
    if user.get(m.chat.id) == '1':
        url = fma1
    elif user.get(m.chat.id) == '2':
        url = fma3
    old = list(m.text.split(', '))
    otvet = a(1, url, old)
    bot.send_message(m.chat.id, "{}".format(otvet))


bot.enable_save_reply_handlers(delay=1)

bot.polling(timeout=60)
