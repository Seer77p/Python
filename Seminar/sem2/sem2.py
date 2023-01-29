# print(4**0.5) Извлечение корня из 4 равное math.sqrt(4)
# pip freeze > requiremennts.txt создает файл txt
# в котором пишутся нужные библиотеки

# Циклы:
# a = 0
# while a < 5:
#     print(a, 'hello')
#     a += 1

# summ = 0
# current_numder = 1
# while current_numder < 11:
#     summ += current_numder
#     current_numder += 1
# print(current_numder, summ)

# for i in range(1, 11, 2): # от 1 до 10 с шагом 2
#     print(i)

# # for i in 1, 7, 10, 15): # выведет 1 7 10 15

# for i in range(11, 1, -2): # считает от 11 до 1 с шагом 2
#     print(i)

# for i in 'one', 'two', 'three', 'four', 4, 7:
#     print(i)

# for i in 'abracadabra':
#     print(i) печать букв

# text = 'Hello'
# for i in range(len(text)):
#     print(i, text[i]) печать номера и текста

# for i in text:
#     print(i, end=' ') печать в одну строку без переноса

# summ = 0
# current_numder = 1
# while current_numder < 11:
#     summ += current_numder
#     current_numder += 1       else не сработает из за прерывания
#     break
# else:
#     print('bye')
# print(current_numder, summ)

# Задачи
# №1 По данному целому неотрицательному n вычислите
# значение n!. N! = 1 * 2 * 3 * … * N (произведение всех
# чисел от 1 до N) 0! = 1 Решить задачу используя цикл
# while
# Input: 5
# Output: 120
# n = int(input('Введите число n: '))
# some_digit = 1
# count = 1
# while 0 < count <= n:
#     print(some_digit)
#     count += 1
#     some_digit *= count


# №2 Дано натуральное число A > 1. Определите, каким по
# счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не
# является числом Фибоначчи, выведите число -1.
# Input: 5
# Output: 6
# 0 1 1 2 3 5 8 13 число
# 0 1 2 3 4 5 6 7  номер числа

# n = int(input('введите число: '))
# count = 3
# if n < 0:
#     print(-1)
# elif n == 0:
#     print(1)
# elif n == 1:
#     print(2)
# else:
#     fib1 = fib2 = 1
#     while fib2 < n:
#         fib3 = fib1 + fib2
#         count += 1
#         fib1 = fib2
#         fib2 = fib3
#     if n == fib2:
#         print(count)
#     else:
#         print(-1)

# Задача №15. Решение в группах
# 15. Иван Васильевич пришел на рынок и решил
# купить два арбуза: один для себя, а другой для тещи.
# Понятно, что для себя нужно выбрать арбуз
# потяжелей, а для тещи полегче. Но вот незадача:
# арбузов слишком много и он не знает как же выбрать
# самый легкий и самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество
# арбузов. Вторая строка содержит N чисел,
# записанных на новой строчке каждое. Здесь каждое
# число – это масса соответствующего арбуза
# Input: 5 -> 5 1 6 5 9
# Output: 1 9

# n = int(input())
# maxi = 0
# mini = 10**100
# for i in range(n):
#     a = int(input())
#     if a > maxi:
#         maxi = a
#     if a < mini:
#         mini = a
# print('Максимальный=', maxi)
# print('Минимальный=', mini)
# print(max(1, 1000))
# print(min(5, 1000))
