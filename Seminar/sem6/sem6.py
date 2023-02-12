# Напишите программу, которая на вход принимает
# два числа A и B, и возводит число А в целую степень B с
# помощью рекурсии.

# def power(a,b):
#     result=1
#     for _ in range(b):
#         result*=a
#     return result

# a=int(input('1'))
# b=int(input('2'))
# print(power(a,b))

# def power(a,b):
#     if b==0:
#         return 1
#     return a*power(a,b-1)

# a=int(input('1 = '))
# b=int(input('2 = '))
# print(power(a,b))

# my_list=[]
# st = input()
# for i in st.split():
#     my_list.append(int(i))

# my_list=[int(i) for i in input().split(',')] #ввод данных в строку в типе int
# print(my_list)
# st=' '.join(my_list)#для строки из списка

# my_list=[[1,2,3],
#          [4,5,6],
#          [7,8,9]]
# for elem in my_list:
#     if isinstance(elem, list):
#         for i in elem:
#             print('list111', elem)
#     elif isinstance(elem,int):
#         print('int', elem)
#     print(elem)
#     for number in elem:
#         print(number)

# my_list=[[j*3 for j in range(i+1, i+3) ]for i in range(5) if i%2==0]#вложенный j
# print (my_list)

# import my_funcs #1 вариант
# from my_funcs import summa#вызывает конкретную функцию можно через запятую

# a=2
# b=3
# print(my_funcs.summa(a,b))


# from my_funcs import * #можно все функции использовать
# def input_data():
#     pass

# def main():
#     n = input_data()

# if __name__=='__main__':
#     main()

# from Python.Seminar.sem6.my_funcs import summa
# print(summa())

# from my_funcs import sum as my_sum  # псевдоним
# def input_data():
#     print(my_sum())

# from my_funcs import summa as su #более короткое написание функции для удобства

# Даны два массива чисел. Требуется вывести те элементы
# первого массива (в том порядке, в каком они идут в первом
# массиве), которых нет во втором массиве. Пользователь вводит
# число N - количество элементов в первом массиве, затем N
# чисел - элементы массива. Затем число M - количество
# элементов во втором массиве. Затем элементы второго массива
# Ввод:               Вывод:
# 7                   3 3 2 12
# 3 1 3 4 2 4 12
# 6
# 4 15 43 1 15 1 

# my_list1 = [3, 1, 3, 4, 2, 4, 12]
# my_list2 = [4, 15, 43, 1, 15, 1]
# out = []
# for i in my_list1:
#     if my_list2.count(i) == 0:
#         out.append(i)
# print(out)

#2
# def sort_of_digits(lisst1, lisst2):
#     final_list = []
#     lisst2 = set(lisst2)
#     for i in range(len(lisst1)):
#         if lisst[i] not in lisst2:
#             final_list.append(lisst1[i])
#     return final_list


# first_list = [3, 1, 3, 4, 2, 4, 12]
# second_list = [4, 15, 43, 1, 15, 1]
# print(sort_of_digits(first_list, second_list))




# Дан массив, состоящий из целых чисел. Напишите
# программу, которая в данном массиве определит
# количество элементов, у которых два соседних и, при
# этом, оба соседних элемента меньше данного. Сначала
# вводится число N — количество элементов в массиве
# Далее записаны N чисел — элементы массива. Массив
# состоит из целых чисел.
# Ввод: Ввод:
# 5                     5
# 1 2 3 4 5             1 5 1 5 1
# Вывод:                Вывод:
# 0                     2

# def check(list_):
#     count = 0
#     for i in range(1, len(list_) - 1):
#         if list_[i-1] < list_[i] > list_[i+1]:
#             count += 1
#     return count
    
# list1 = [1, 2, 3, 4, 5]
# list2 = [1, 5, 1, 5, 1]
# print(check(list1))
# print(check(list2))

# Дан список чисел. Посчитайте, сколько в нем пар
# элементов, равных друг другу. Считается, что любые
# два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать. Вводится список
# чисел. Все числа списка находятся на разных
# строках.
# Ввод:              Вывод:
# 1 2 3              2 3 2
# a=[2,2,2,2]
# count=0
# for i in range(len(a)-1):
#     for j in range(i+1, len(a)):
#         if a[i]==a[j]:
#             count+=1
# print(count)
