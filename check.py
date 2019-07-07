import urllib.request
from html_table_parser import HTMLTableParser


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
    f = urllib.request.urlopen(req)
    return f


def parse(url):
    abit = []
    xhtml = url_get_contents(url).read().decode('utf-8')
    p = HTMLTableParser()
    a = p.feed(xhtml)
    new = list(p.tables)
    del new[0]  # удалить окно поиска на сайте нгту
    del new[0][0:3]  # удалить шапку талицы
    # print(new[0])
    # print(len(new[0]))
    for i in new[0]:
        #print(len(i))
        abit.append(i[1] if len(i) > 1 else i[0])
    return abit


def answer(method, url='', text=''):
    if method == 1:
        old = list(text)
        new = parse(url)
        return find(new, old)
    if method == 2:
        fma = parse('https://www.nstu.ru/enrollee/entrance/entrance_list?competition=4397')
        fen = parse('https://www.nstu.ru/enrollee/entrance/entrance_list?competition=4414')
        return net_fma(fen, fma)

