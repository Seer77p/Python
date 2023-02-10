# dz-4.6
# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств.
# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# 6 12
from random import randint, random

spisok_a = list()
spisok_b = list()
list_size = int(input('Введите размер списка №1: '))
list_size2 = int(input('Введите размер списка №2: '))
while list_size == 0 or list_size2 == 0:
    print('Введенный размер списка №1', list_size, 'не может быть нулевым')
    print('Введенный размер списка №2', list_size2, 'не может быть нулевым')
    list_size = int(input('Введите размер списка №1: '))
    list_size2 = int(input('Введите размер списка №2: '))
for i in range(list_size):
    spisok_a.append(randint(1, 20))
for i in range(list_size2):
    spisok_b.append(randint(1, 20))
print('Исходные элементы последовательности №1', '     ', spisok_a, end='')
print()
print('Исходные элементы последовательности №2', '     ', spisok_b, end='')
unique_bunch_a = (set(spisok_a))
unique_bunch_b = (set(spisok_b))
print()
print('Уникальные элементы последовательности №1', '   ', unique_bunch_a, end='')
print()
print('Уникальные элементы последовательности №2', '   ', unique_bunch_b, end='')
intersection_list = unique_bunch_a.intersection(unique_bunch_b)
print()
print('В Обоих списках встречаются одинаковые числа ', sorted(intersection_list))
