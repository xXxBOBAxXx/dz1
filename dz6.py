# 1 -  Написать программу вычисления арифметического выражения заданного строкой. Используются операции +,-,/,*.
# приоритет операций стандартный. Функцию eval не использовать!
# Пример: 2+2 => 4; 1+2*3 => 7; 1-2*3 => -5;
# Дополнительно: Добавить возможность использования скобок, меняющих приоритет операций. 
# Пример: 1+2*3 => 7; (1+2)*3 => 9;
import re

def calc(string: str) -> str:
    actions = {'*': lambda x, y: str(float(x) * float(y)),
        '/': lambda x, y: str(float(x) / float(y)),
        '+': lambda x, y: str(float(x) + float(y)),
        '-': lambda x, y: str(float(x) - float(y))}

    priority = r'\((.+?)\)'
    act_reg = r'(-?\d+(?:\.\d+)?)\s*\{}\s*(-?\d+(?:\.\d+)?)'

    while (match := re.search(priority, string)):
        string: str = string.replace(match.group(0), calc(match.group(1)))
    for j, i in actions.items():
        while (match := re.search(act_reg.format(j), string)):
            string: str = string.replace(match.group(0), i(*match.groups()))
    if string[-2:] == '.0': return string[:-2]
    else: return string
    
print(calc(input('Введите строку: ')))

# 2 - Реализовать RLE алгоритм. реализовать модуль сжатия и восстановления данных. 
# Входные и выходные данные хранятся в отдельных файлах (в одном файлике отрывок из какой-то книги, а втором файлике — сжатая версия этого текста). 
def rle_encode(string):
    encode = ''
    prev = ''
    count = 1
    if not string: return ''
    for i in string:
        if i != prev:
            if prev: encode += str(count) + prev
            count = 1
            prev = i
        else: count += 1
    else:
        encode += str(count) + prev
        return encode

def rle_decode(result):
    decode = ''
    count = ''
    for i in result:
        if i.isdigit(): count += i
        else:
            decode += i * int(count)
            count = ''
    return decode

with open('text for dz6.txt', 'r') as file: string = file.read()
print(string)
result = rle_encode(string)
print(result)
with open('text2 for dz6.txt', 'w') as file: string = file.write(result)
string = rle_decode(result)
print(string)

# 3 -  ROT13 - это простой шифр подстановки букв, который заменяет букву буквой, которая идет через 13 букв после нее в алфавите. 
# ROT13 является примером шифра Цезаря.
# Создайте функцию, которая принимает строку и возвращает строку, зашифрованную с помощью Rot13 . 
# Если в строку включены числа или специальные символы, они должны быть возвращены как есть. 
# Также создайте функцию, которая расшифровывает эту строку обратно (некий начальный аналог шифрования сообщений). 
# Не использовать функцию encode.
def rot13(string, regime):
    decode = 'аАбБвВгГдДеЕёЁжЖзЗиИйЙкКлЛмМнНоОпПрРсСтТуУфФхХцЦчЧшШщЩъЪыЫьЬэЭюЮяЯ'
    encode = 'мМнНоОпПрРсСтТуУфФхХцЦчЧшШщЩъЪыЫьЬэЭюЮяЯаАбБвВгГдДеЕёЁжЖзЗиИйЙкКлЛ'

    if regime == 'encode': coding = dict(zip(decode, encode))
    if regime == 'decode': coding = dict(zip(encode, decode))
    return ''.join(coding.get(i, i) for i in string)

string = rot13(input('Введите строку: '), 'encode')
print(string)
string = rot13(string, 'decode')
print(string)
