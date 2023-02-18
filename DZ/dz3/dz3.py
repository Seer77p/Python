# pip freeze > requiremennts.txt

# dz-3.1
# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
# стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
from random import randint, random

spisok = list()
list_size = int(input('Введите размер списка: '))
while list_size == 0:
    print('Введенный размер списка', list_size, 'не может быть нулевым')
    list_size = int(input('Введите размер списка: '))
for i in range(list_size):
    spisok.append(randint(1,9))
    print('Элемент списка от 0 до', i,'  ', spisok[i])
summ=0
for i in range(1, list_size, 2):
    summ+=spisok[i]
print('Сумма чисел стоящих на нечетных позициях = ',summ)

# dz-3.2
# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]
spisok_3_2 = list()
list_size_3_2 = int(input('Введите размер списка: '))
while list_size_3_2 == 0:
    print('Введенный размер списка', list_size_3_2, 'не может быть нулевым')
    list_size_3_2 = int(input('Введите размер списка: '))
for i in range(list_size_3_2):
    spisok_3_2.append(randint(1,9))
    print('Элемент списка от 0 до', i,'  ', spisok_3_2[i])
proizvedenie = 1
if (list_size_3_2%2==0): cout=list_size_3_2/2
else: cout=int(list_size_3_2//2)+1
for i in range(int(cout)):
    if i==(-i+1):
        proizvedenie*=spisok_3_2[i]
    else:
        proizvedenie=spisok_3_2[i]*spisok_3_2[-1*(i+1)]
    print('Произведение', proizvedenie)


# dz-3.3
# Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным
# значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

spisok_3_3 = list()
list_size_3_3 = int(input('Введите размер списка: '))
while list_size_3_3 == 0:
    print('Введенный размер списка', list_size_3_3, 'не может быть нулевым')
    list_size_3_3 = int(input('Введите размер списка: '))
# Заполнение списка, и отбрасываем целую часть
for i in range(list_size_3_3):
    spisok_3_3.append(round(random()*20, 3))
    print('Случайное вещественное число:', i+1, ' = ', spisok_3_3[i],',  ', end= '  ')
    spisok_3_3[i]=round(spisok_3_3[i]-int(spisok_3_3[i]),3)
    print('Число без целой части =', spisok_3_3[i])
print()
print('Максимальное число ', max(spisok_3_3), '- Минимальное число ', min(spisok_3_3),'=', max(spisok_3_3)-min(spisok_3_3))


# dz-3.4
# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10
binary_number = list()
decimal = int(input('Введите положительно целое число: '))
while 0 > decimal or decimal== 0:
    print('Число не является положительным или равно 0', decimal)
    decimal = int(input('Введите положительно целое число: '))
# Преобразование числа в двоичную систему
i=0
while decimal!=0:
    binary_number.append(decimal%2)
    decimal//=2
revers_num=list()
for i in range(len(binary_number)):
    revers_num.append(binary_number[(i+1)*-1])
print(revers_num[:], end=' ')
print()


# dz-3.5
# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
# list_size_3_5 = int(input('Введите количество чисел Фибоначи: '))
# while list_size_3_5 == 0:
#     print('Введенное количество', list_size_3_5, 'не предполагает расчет')
#     list_size_3_5 = int(input('Введите количество чисел Фибоначи: '))
# spisok_3_5 = [0]*(list_size_3_5*2+1)
# spisok_3_5[list_size_3_5+1] = 0
# positive = [0]*(list_size_3_5)
# negative = [0]*(list_size_3_5)
# for i in range(list_size_3_5):
#     if i > 1:
#         positive[i] = positive[i-2]+positive[i-1]
#         negative[i] = negative[i-2]-negative[i-1]
#     if i == 0:
#         positive[i] = 1
#         negative[i] = 1
#     if i == 1:
#         positive[i] = 0+positive[i-1]
#         negative[i] = 0-negative[i-1]
# for i in range(list_size_3_5):
#     spisok_3_5[i] = negative[(list_size_3_5-1)-i]
#     spisok_3_5[i+list_size_3_5+1] = positive[i]
# print(spisok_3_5, end=' ')
# print()

fibo = [1, 0, 1]
for i in range(10):
    next_ = fibo[-1] + fibo[-2]
    fibo.append(next_)
    prev_ = fibo[1] - fibo[0]
    fibo.insert(0, prev_)
print(fibo)

# dz-3.6
# Задача 16: Требуется вычислить, сколько раз встречается некоторое
# число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел Ai.
# Последняя строка содержит число X
# 5
# 1 2 3 4 5
# 3
# -> 1
list_size_3_6 = int(input('Введите размер списка: '))
while list_size_3_6 == 0:
    print('Введенный размер списка', list_size_3_6, 'не может быть нулевым')
    list_size_3_6 = int(input('Введите размер списка: '))
spisok_3_6 = list()
for i in range(list_size_3_6):
    spisok_3_6.append(randint(1,9))
print('Элементы списка от 1 до', i+1,'  ', spisok_3_6)

desired_number = int(input('Введите искомое число (от 1 до 9): '))
while 0 >= desired_number or desired_number > 9:
    print('Введенное число меньше или равно 0, либо больше 9 ', desired_number)
    list_size_3_6 = int(input('Введите искомое число (от 1 до 9): '))
summ=0
for i in range(list_size_3_6):
    if spisok_3_6[i] == desired_number: summ+=1
print('Количество искомых чисел в списке=', summ)

# dz-3.7
# Задача 18: Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai. Последняя строка
# содержит число X
# 5
# 1 2 3 4 5
# 6
# -> 5
list_size_3_7 = int(input('Введите размер списка: '))
while list_size_3_7 == 0:
    print('Введенный размер списка', list_size_3_7, 'не может быть нулевым')
    list_size_3_7 = int(input('Введите размер списка: '))
spisok_3_7 = list()
for i in range(list_size_3_7):
    spisok_3_7.append(randint(1,9))
print('Элементы списка от 1 до', i+1,'  ', spisok_3_7)
desired_number = int(input('Введите искомое число: '))
summ=0
for i in range(list_size_3_7):
    if spisok_3_7[i] == desired_number: summ+=1
if desired_number<1: print('Ближайшее число к искомому числу',min(spisok_3_7))
if desired_number>9: print('Ближайшее число к искомому числу',max(spisok_3_7))
if summ!=0: print('Количество искомых чисел в списке = ', summ)



