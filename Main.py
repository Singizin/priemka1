import telebot
from telebot.types import Message
from telebot import types
from telebot import apihelper
from check import answer as a
from check import now
from check import *
from databaseHeroku import *
fma1 = 'https://www.nstu.ru/entrance/admission_campaign/entrance/entrance_list?competition=4829'  # Энергетика
fen1 = 'https://www.nstu.ru/entrance/admission_campaign/entrance/entrance_list?competition=4841'  # Энергетика
fma3 = 'https://www.nstu.ru/entrance/admission_campaign/entrance/entrance_list?competition=4831'  # Автоматизация
fma2 = 'https://www.nstu.ru/entrance/admission_campaign/entrance/entrance_list?competition=4830'  # Энергетика ммрк

TOKEN = '747611758:AAEpFP3iLMCbtmrLF0omSyTnjP7d7CCIaPY'
bot = telebot.TeleBot(TOKEN)
bot.send_message(260119686, "Go")
global user
user = {}

keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard.add('/fen', '/check', '/escape')


@bot.message_handler(commands=['fma1check'])
def fma1check(message: Message):
    bot.send_message(message.from_user.id, find(parse(fma1), fma1Select()))

@bot.message_handler(commands=['fma1consent'])
def fma1consent(message: Message):
    bot.send_message(message.from_user.id, find(parseConsent(fma1 + '&o_only=2'), fma1consentSelect()))

@bot.message_handler(commands=['fma2consent'])
def fma1consent(message: Message):
    bot.send_message(message.from_user.id, find(parseConsent(fma2 + '&o_only=2'), fma2consentSelect()))

@bot.message_handler(commands=['fma3check'])
def fma3check(message: Message):
    bot.send_message(message.from_user.id, find(parse(fma3), fma3Select()))

@bot.message_handler(commands=['fma3consent'])
def fma3consent(message: Message):
    print('fma3')
    bot.send_message(message.from_user.id, find(parseConsent(fma3 + '&o_only=2'), fma3consentSelect()))

@bot.message_handler(commands=['fen1check'])
def fen1check(message: Message):
    bot.send_message(message.from_user.id, find(parse(fen1), fen1Select()))

@bot.message_handler(commands=['fma1update'])
def fma1update(message: Message):
    newFma1(parse(fma1))
    bot.send_message(message.from_user.id, 'список для ФМА 13.03.02 обновлен')

@bot.message_handler(commands=['fma1consentupdate'])
def fma1consentupdate(message: Message):
    newFma1consent(parseConsent(fma1 + '&o_only=2'))
    bot.send_message(message.from_user.id, 'список для ФМА 13.03.02 обновлен согласия')

@bot.message_handler(commands=['fma3update'])
def fma3update(message: Message):
    newFma3(parse(fma3))
    bot.send_message(message.from_user.id, 'список для ФМА 15.03.04 обновлен')

@bot.message_handler(commands=['fma3consentupdate'])
def fma1consentupdate(message: Message):
    print('fma3c')
    newFma3consent(parseConsent(fma3 + '&o_only=2'))
    bot.send_message(message.from_user.id, 'список для ФМА 15.03.04 обновлен согласия')

@bot.message_handler(commands=['fen1update'])
def fen1update(message: Message):
    newFen1(parse(fen1))
    bot.send_message(message.from_user.id, 'список для ФЭН 13.03.02 обновлен')

@bot.message_handler(commands=['fma2consentupdate'])
def fma2consentupdate(message: Message):
    newFma2consent(parseConsent(fma2 + '&o_only=2'))
    bot.send_message(message.from_user.id, 'список для ФМА 13.03.02 ММРК обновлен согласия')

@bot.message_handler(commands=['fenbezfma'])
def command_handler(message: Message):
    count, spisok = a()
    bot.send_message(message.from_user.id, count)
    bot.send_message(message.from_user.id, spisok)

'''
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
'''

# bot.enable_save_reply_handlers(delay=1)


bot.polling(timeout=60)
