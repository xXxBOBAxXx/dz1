# 1. Напишите программу, удаляющую из текста все слова содержащие "абв", которое регистронезависимо. 
# Используйте знания с последней лекции. Выполните ее в виде функции. 
# Пример: «абвгдеж рабав копыто фабв Абкн абрыволк аБволк»
def abv(str, fragment):
    words = str.split(' ')
    rslt = []
    for word in words:
        if fragment not in word.casefold():
            rslt.append(word)
    rslt = ' '.join(rslt)        
    return rslt

print(abv('абвгдеж рабав копыто фабв Абкн абрыволк аБволк', 'абв'))


# 2. Вы когда-нибудь играли в игру "Крестики-нолики"? Попробуйте создать её, причем чтобы сыграть в нее можно было в одиночку. 
def board(cages):
    for i in range(3):
        print(cages[0+i*3], cages[1+i*3], cages[2+i*3])

def step(count):
    complete = False
    while not complete:
        player = input("Выберете номер клетки: ")
        try:
            player = int(player)
        except:
            print("Нет клетки с таким номером")
            continue
        if player >= 1 and player <= 9:
            if(str(cages[player - 1]) not in "xo"):
                cages[player - 1] = 'x'
                complete = True
            else:
                print("Эта клетка уже выбрана")

    complete = False
    while not complete:
        if count < 4:
            computer = randint(1, 9)
            if(str(cages[computer - 1]) not in "xo"):
                cages[computer - 1] = 'o'
                complete = True
        else:
            complete = True
    
def win(cages):
    lines = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
    for i in lines:
        if cages[i[0]] == cages[i[1]] == cages[i[2]] == 'x':
            winner = 'Вы выйграли'
            return winner
        if cages[i[0]] == cages[i[1]] == cages[i[2]] == 'o':
            winner = 'Выйграл компьютер'
            return winner

def main(cages):
    count = 0
    while count < 5:
        step(count)
        board(cages)
        count += 1
        if count > 2:
            winner = win(cages)
            if winner:
                print(winner)
                break
        if count == 5:
                print('Ничья')
                break

from random import randint
cages = list(range(1,10))
board(cages)
main(cages)


# 3. Вот вам текст:
novel = '''Ну, вышел я, короче, из подъезда. В общем, короче говоря, шел я, кажется, в магазин. Ну,эээ, в общем, было лето, кажется. Как бы тепло. Солнечно, короче. Иду я, иду, в общем, по улице, а тут, короче, яма. Я, эээээ…. Упал в нее. И снова вышел, короче, из подъезда. Ясен пень, в магазин. В общем, лето на дворе, жарко, солнечно, птицы, короче, летают. Кстати, иду я по улице, иду, а тут, короче, яма. Ну, я в нее упал, в общем. Вышел из подъезда, короче. Лето на дворе, ясен пень. Птицы поют, короче, солнечно. В общем, в магазин мне надо. Что-то явно не так, короче. «Рекурсия», - подумал я. Ээээ...короче, в общем, пошел другой дорогой и не упал в эту… ээээ… яму. Хлеба купил.'''
# Отфильтруйте его, чтобы этот текст можно было нормально прочесть. 
# Предусмотрите вариант, что мусорные слова могли быть написаны без использования запятых.

trash = ('ну', 'короче говоря', 'в общем', 'короче', 'кажется', 'как бы', 'ясен пень', 'эээ', 'ээ', '…', '...', ',')
novel = novel.lower()
for str in novel.split('\n'):
    for i in trash:
        str = str.replace(i, '')
str = str.replace(' э ', ' ')
str = str.replace(' э,', ' ')
str = str[0:-1].replace('.', ',') + str[-1]
str = str.replace(' ,', ',')
str.split()
print(' '.join(str.split()).capitalize())
