# Найти НОК двух чисел
a, b = 10, 15
def LCM(a, b):
    if b == 0:
        return a
    return LCM(b, a % b)
print(a * b // LCM(a, b))

# Вычислить число Пи c заданной точностью d
# Пример: при d = 0.001,  c= 3.141. 
import math
d = str(input('Введите число: '))
cnt = 0
for i in range(len(d)):
    if cnt > 0:
        cnt += 1
    if d[i] == '.':
        cnt += 1
print(round(math.pi, cnt - 1))

# Составить список простых множителей натурального числа N
N = (input('Введите число: '))
lst = []
if N % 2 == 0:
    for i in range(0, N, 2):
        lst.append(2)
elif N % 3 == 0:
    for i in range(0, N, 3):
        lst.append(3)  
else:
    for i in range(0, N, 1):
        lst.append(1)
print(lst)

# Дана последовательность чисел. Получить список неповторяющихся элементов исходной последовательности
# Пример: [1, 2, 3, 5, 1, 5, 3, 10] => [1, 2, 3, 5, 10]
nums = [1, 2, 3, 5, 1, 5, 3, 10]
unq = []
for i in nums:
    if i not in unq:
        unq.append(i)
print(unq)

# 5.  Дан текстовый файл, содержащий целые числа. Удалить из него все четные числа. 
with open('nums for dz3.txt', 'w') as file:
    for i in range(1,1+9):
        file.write(str(i) + '\n')

with open('nums for dz3.txt', 'r') as file:
    list = []
    for i in file:
        if int(i) % 2 == 1:
            list.append(int(i))
            
with open('nums for dz3.txt', 'w') as file:
    for i in range(len(list)):
        file.write(str(list[i]) + '\n')