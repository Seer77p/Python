# Урок 2. Циклы (for, while)
# dz-2.1
# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11
from random import randint
real_number = str(input('Введите вещественное число: '))
real_number = real_number.replace('.', '')
summ = 0
for i in real_number:
    summ += int(i)
print('Сумма цифр в числе =', summ)

# dz2.2
# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

number_of_works = int(input('Введите число n: '))
product_of_numbers = 1
count = 1
while 0 < count <= number_of_works:
    print('Набор произведений чисел от 1',
          'до', count, '=', product_of_numbers)
    count += 1
    product_of_numbers *= count

# dz2.3
# Задайте список из n чисел последовательности (1+1/n)**n и выведите на экран их сумму.
# Пример:
# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}
sequence_n = int(input('Ведите N для последовательности чисел: '))
for i in range(1, sequence_n+1):
    print(round(float((1+1/i)**i), 3), end='    ')
print('\n')

# dz.2.4
# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt
# в одной строке одно число.

# Создание списка и его заполнение случайными числами в диапазоне от -N до N
size = int(input('Введите количество элементов N: '))
while size == 0:
    print('Введенное количество', size, '0 элементов, нечего считать N')
    size = int(input('Введите количество элементов N: '))
list_elements = []
for i in range(size):
    list_elements.append(randint(-size, size))
    print('Элемент', i+1, 'равен: ', list_elements[i])
# Запись элументов списка в фвйл txt
with open(r"file.txt", "w") as file:
    for i in list_elements:
        file.write(str(i) + '\n')
# Чтение значения заданных элементов и их произведение
number_element1 = int(
    input('Введите позицию из которой будет взят елемент 1 для умножения: '))
while number_element1 <= 0 or number_element1 > size:
    number_element1 = int(input(
        'Порядковый номер элемента не может быть отрицательным, равен 0, превышать заданноe количество элементов, введите позицию 1 '))
number_element2 = int(
    input('Введите позицию из которой будет взят елемент 2 для умножения: '))
while number_element2 <= 0 or number_element2 > size:
    number_element2 = int(input(
        'Порядковый номер элемента не может быть отрицательным, равен 0, превышать заданноe количество элементов, введите позицию 2'))
with open(r"file.txt", "r") as file:
    lines = file.readlines()
print('Произведение 1-го и 2-го чисел равно',
      int(lines[number_element1-1])*int(lines[number_element2-1]))


# dz.2.5
# Реализуйте алгоритм перемешивания списка.
print('Распечатка списка')
mixing = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in range(len(mixing)):
    print(mixing[i], end='  ')
temp = 0
for i in range(len(mixing)):
    index = randint(0, 9)
    temp = mixing[i]
    # print(index)
    mixing[i] = mixing[int(index)]
    # print(index)
    mixing[index] = temp
print('\n')
for i in range(len(mixing)):
    print(mixing[i], end='  ')
print('\n')

# dz-2.6
# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх
# решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.
# 5 -> 1 0 1 1 0
# 2

size = int(input('Введите количество монет: '))
while size <= 0:
    print('Количество монет не может быть отрицательным или буть нулевым, нечего считать N')
    size = int(input('Введите количество монет: '))
coins = []
taiks = 0
eagle = 0
for i in range(size):
    coins.append(randint(0, 1))
    if (coins[i] == 0):
        taiks += 1
    else:
        eagle += 1
    print(coins[i], end=' ')
print('\n')
if taiks > eagle:
    print('Минимальное количество монет, которые надо перевернуть лежат гербом вверх', eagle)
elif taiks < eagle:
    print('Минимальное количество монет, которые надо перевернуть лежат решкой вверх', taiks)
else:
    print('Количество монет одинаково')
print('\n')

# dz-2.7
# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя –
# школьница. Петя помогает Кате по математике. Он задумывает два
# натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для
# этого Петя делает две подсказки. Он называет сумму этих чисел S и их
# произведение P. Помогите Кате отгадать задуманные Петей числа.
# 4 4 -> 2 2
# 5 6 -> 2 3
number_one = int(input('Введите первое число: '))
while 0 > number_one or number_one == 0 or number_one > 1000:
    print('Введенное число равно нулю, отрицательное, либо больше 1000')
    number_one = int(input('Введите 1 число больше 0: '))
number_two = int(input('Введите второе число: '))
while 0 > number_two and number_two == 0 and number_two > 1000:
    print('Введенное число равно нулю, отрицательное, либо больше 1000')
    number_two = int(input('Введите 2 число больше 0: '))
summ = number_one+number_two
multiplication = number_one*number_two
print('Сумма двух чисел =', int(summ))
print('Произведение двух чисел =', int(multiplication))
for i in range(1, summ):
    if ((summ-i)*i) == multiplication:
        print('Загаданные числа', int(summ-i), 'и', int(summ-(summ-i)))
        break

# dz-2.8
# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k),
# не превосходящие числа N.

degree = int(input('Введите до которого будут выдаваться степени 2: '))
while degree <= 0:
    print('Введите число больше нуля')
temp = 0
number_to_the_power = 0
while number_to_the_power < degree:
    number_to_the_power = 2**temp
    print('Целая часть степени 2 **', temp, '=', number_to_the_power)
    temp += 1
    if (2**temp) > degree:
        number_to_the_power = degree
