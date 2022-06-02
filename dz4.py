# 1. Дан список чисел. Создать список, в который попадают числа, описываемые возрастающую последовательность. 
# Пример: [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д. Порядок элементов менять нельзя
from random import randint
list = [1, 5, 2, 3, 4, 6, 1, 7]
new_list = []
new_list.append(list[0])

for i in range(1, len(list)):
    if list[i] > list[i-1] and list[i] > new_list[-1]:
        if randint(0, 1) == 1:
            new_list.append(list[i])

while len(new_list) == 1:
    if list[i] > new_list[-1]:
        new_list.append(list[i])
    else:
        i -= 1
print(new_list)

# 2. Создать и заполнить файл случайными целыми значениями. Выполнить сортировку содержимого файла по возрастанию. 
with open('nums for dz4.txt', 'w') as file:
    for i in range(randint(2, 9)):
        i = randint(0, 9)
        file.write(str(i) + '\n')

with open('nums for dz4.txt', 'r') as file:
    list = []
    for i in file:
        list.append(int(i))
list.sort()

with open('nums for dz4.txt', 'w') as file:
    for i in range(len(list)):
        file.write(str(list[i]) + '\n')
        
# 3. Задача: найти триплеты и просто выводить их на экран. 
# Триплетом называются три числа, которые в сумме дают 0. 
# (решение будет долгим, ибо является демонстрационным при теме многопоточного программирования). 
with open('1Kints.txt', 'r') as file:
    list = []
    for i in file:
        list.append(int(i))
        
for i in range(len(list) - 1):
    triplet = []
    for j in range(i + 1, len(list)):
        num3 = -(list[i] + list[j])
        if num3 in triplet:
            print(list[i], list[j], num3)
        else:
            triplet.append(list[j])