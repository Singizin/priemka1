import urllib.request
import requests
from html_table_parser import HTMLTableParser
import pandas as pd
import databaseHeroku

def find(new, old):
    '''
    :param new: новый список с сайта
    :param old: старый список из сообщения выше
    :return: возвращает разницу в виде сообщения
    '''
    leave = []
    come = []
    for i in new:
        if i not in old:
            come.append(i)
    for i in old:
        if i not in new:
            leave.append(i)
    s = 'Новых людей - {}:\n{}\nУшло людей - {}:\n{}'.format(len(come),come,len(leave), leave)
    return s


def bez_kovich(s):
    now = ''
    for i in s:
        now = now + '{}{}'.format(', 'if now != '' else '', i)
    return now


def net_fma(fen, fma):
    '''
    Возвращает список всех кто есть в первом списке и нет во втором
    :param fen:
    :param fma:
    :return:
    '''
    net = []
    for i in fen:
        if i not in fma:
            net.append(i)
    s = 'Можно добавить нашу энергетику {} людям:\n'.format(len(net))
    return s, bez_kovich(net)


def now(url):
    return bez_kovich(parse(url))


def url_get_contents(url):
    """ Opens a website and read its binary contents (HTTP Response Body) """
    req = urllib.request.Request(url=url)
    f = requests.get(url).content.decode()
    #print(f)
    #f = f.content.decode()
    return f


def parse(url):
    abit = []
    xhtml = url_get_contents(url)
    table = pd.read_html(xhtml)
    df = table[0]
    new = df.values.tolist()
    del new[0]
    flag = False
    for i in new:
        if i[1] == 'По конкурсу':
            flag = True
            continue
        if i[1] == "Не выдержавшие вступительные испытания":
            break
        if flag:
            abit.append(i[1] if len(i) > 1 else i[0])
    return abit


def answer():
    fma = parse('https://www.nstu.ru/entrance/admission_campaign/entrance/entrance_list?competition=4829')  # Энергетика
    fen = parse('https://www.nstu.ru/entrance/admission_campaign/entrance/entrance_list?competition=4841')
    return net_fma(fen, fma)
