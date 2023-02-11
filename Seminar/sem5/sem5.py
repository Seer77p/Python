# def summa():
#     b = a+1
#     return b
# a = 5
# n = summa()
# print(n)

# def summa():    так не работает
#     a = a + 1
#     return a
# a = 5
# n = summa()
# print(n)

# def summa(*args, **kwargs):
#     print(args)
#     a,*b,c=args
#     print(kwargs)
#     print(a,c)
#     print(b)

#     return 0

# n=summa(1,2,3,4,5, name ='Vas', key='sort')

# def input_data():
#     pass
# def solve(a,b):
#     pass
# def output_data(a):
#     pass
# a,b=input_data()
# answer=solve(a,b)
# output_data(answer)

# def factorial(n):
#     if n == 1:

#         return 1
#     return n*factorial(n-1)
# print(factorial(10))

# Задача №31. 
# Последовательностью Фибоначчи называется
# последовательность чисел a0, a1, ..., an, ..., где
#  a0 = 0, a 1= 1, ak = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи
# Input: 7
# Output: 21

# def fib(n):
#     if n<2:
#         return n
#     return (fib(n-1))+fib(n-2)
# for  i in range(30):
#     print (fib(i),' ', end='')

# def fib(n):
#     if n<2:
#         return n
#     return (fib(n-1))+fib(n-2)
# a=[1,1]
# for  i in range(2,100):
#     a.append(a[i-1]+a[i-2])
# print (a,' ', end='')

# def fib(n):
#     if n<2:
#         return n
#     if cashe[n]>0
#     return (fib(n-1))+fib(n-2)
# a=[1,1]
# for  i in range(2,100):
#     a.append(a[i-1]+a[i-2])
# print (a,' ', end='')


# def fib(n):
#     if n in [1, 2]:
#         return 1
#     return fib(n - 1) + fib(n - 2)

# num = int(input('Введите число: '))
# list_1 = [0]
# for i in range(1, num + 2):
#     list_1.append(fib(i))
# print(list_1)
# print(f'{num}-е число Фибоначчи =', list_1[-1])

# №2def numFibinachi(num):
#     if num in [0, 1]:
#         return 1
#     return numFibinachi(num-2) + numFibinachi(num - 1)

# num = int(input("Введите искомое число Фибоначчи: "))
# print(numFibinachi(num))

# Задача №33. 
# Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1
# def grade(array):
#     maxi = max(array)
#     mini = min(array)
#     for i in range(len(array)):
#         if array[i] == maxi:
#             array[i] = mini
#     return array

# print(grade([1, 3, 3, 3, 4]))

# def solve(my_list):
#     new_list=my_list[:]     копирование списка
#     new_list=my_list.copy() копирование списка
#     min_=min(new_list)
#     max_=max(new_list)
#     for i in range(len(new_list)):
#         if new_list[i]==max_:
#             new_list[i]=min_
#     return new_list
# a=[1,2,3,3,4]
# print(solve(a))



# Напишите функцию, которая принимает одно число и
# проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое
# имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes

# numbers = int(input('Введите натуральное число: '))
# number_list = list()
# while numbers != 1:
#     if numbers % 2 == 0:
#         number_list.append(2)
#         numbers //= 2
#     elif numbers % 3 == 0:
#         number_list.append(3)
#         numbers //= 3
#     elif numbers % 5 == 0:
#         number_list.append(5)
#         numbers //= 5
#     elif numbers % 7 == 0:
#         number_list.append(7)
#         numbers //= 7
#     else:
#         number_list.append(numbers)
#         numbers //= numbers
# print('Простые множители введенного числа: ', number_list, end='')