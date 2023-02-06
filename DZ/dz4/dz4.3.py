# dz-4.3
# Задайте последовательность чисел. Напишите программу,
# которая выведет список неповторяющихся элементов исходной последовательности.

from random import randint, random

spisok = list()
list_size = int(input('Введите размер списка: '))
while list_size == 0:
    print('Введенный размер списка', list_size, 'не может быть нулевым')
    list_size = int(input('Введите размер списка: '))
for i in range(list_size):
    spisok.append(randint(1, 9))
print('Исходные элементы последовательности', '    ', spisok, end='')
unique_bunch = (set(spisok))
print()
print('Уникальные элементы последовательности', '  ', unique_bunch, end='')
