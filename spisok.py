
from check import answer as a
from check import parse

#print(a(1,'https://www.nstu.ru/enrollee/entrance/entrance_list?competition=4397'))

# s = parse('https://www.nstu.ru/enrollee/entrance/entrance_list?competition=4397')

def bez_kovich(s):
    now = ''
    for i in s:
        now = now + '{}{}'.format(', 'if now != '' else '', i)
    return(now)

print(a(2))