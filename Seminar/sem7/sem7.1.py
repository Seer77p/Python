# summ = lambda x,y: x+y if x==y else x-y
# print(sum(17,5))

# def calc(a,b, oper):
#     return oper(a,b)

# def summa(a,b):
#     return a+b

# print(calc(4,6, summa))

# my_list=['6', '7', '-8', '4']
# my_list=list(map(lambda x: int(x)+2, my_list))
# print(my_list)

# my_list=['6', '7', '-8', '4']
# my_list=list(map(int, my_list))
# print(my_list)

# my_list=map(int,input().split())
# print('fff', list(my_list)) #fff [5, 6, 2, 1, 4, 7, 8, 8, 3] ввод через пробел

# my_list=['hello', 1,3,4,'hal']
# for i in range(len(my_list)):
#     print(my_list[i])

# for elem in my_list:
#     print(elem)

# for i, elem in enumerate(my_list): #печать кортежа номер - значение

#     print(i, elem, end=' ') #номер, значение 0 hello 1 1 2 3 3 4 4 hal

# i, elem=(5,'hello')
# print()
# print(i, elem,'\n')  # 5 hello

# my_set={1,2,10,6,5,8}
# spisok=list(enumerate(my_list))
# for i, elem in enumerate(my_set):
#     print(i, elem, end=' ')

# my_list=[1,2,3,4,5,6,7, 0, -1, -2, -3, -4]
# my_list2=list(filter(lambda x:x%2==0, my_list))#[2, 4, 6]
# print(my_list2)                                # фильтр по условию

# my_list=[41,22,23,4,53,6,7]
# my_list2=list(map(list(filter(lambda x:x%10==3, my_list))))#[2, 4, 6]
# print(my_list2)

# my_list3=[i for i in my_list if i%10==3]
# print(my_list3)

# def solve(x):
#     return True
# my_list2=list(filter(solve, my_list))#[2, 4, 6]

# a=[1,2,3]
# b=['hello', 'hi', 'bye', 'hehe']
# #c=[True, False, True]

# result=list(zip(a,b))
# print(result)   #[(1, 'hello', True), (2, 'hi', False), (3, 'bye', True)]

# a=[1,2,3]
# b=['hello', 'hi', 'bye', 'hehe']
# #c=[True, False, True]

# result=list(zip(a,b))
# print(dict(result))   #{1: 'hello', 2: 'hi', 3: 'bye'}
#                      #объединили списки и dict сделали список

# Планеты вращаются вокруг звезд по эллиптическим орбитам.
# Назовем самой далекой планетой ту, орбита которой имеет
# самую большую площадь. Напишите функцию
# find_farthest_orbit(list_of_orbits), которая среди списка орбит
# планет найдет ту, по которой вращается самая далекая
# планета. Круговые орбиты не учитывайте: вы знаете, что у
# вашей звезды таких планет нет, зато искусственные спутники
# были были запущены на круговые орбиты. Результатом
# функции должен быть кортеж, содержащий длины полуосей
# эллипса орбиты самой далекой планеты. Каждая орбита
# представляет из себя кортеж из пары чисел - полуосей ее
# эллипса. Площадь эллипса вычисляется по формуле S = pi*a*b,
# где a и b - длины полуосей эллипса. При решении задачи
# используйте списочные выражения. Подсказка: проще всего
# будет найти эллипс в два шага: сначала вычислить самую
# большую площадь эллипса, а затем найти и сам эллипс,
# имеющий такую площадь. Гарантируется, что самая далекая
# планета ровно одна
def find_farthest_orbit(my_list):
    maxi = 0
    kort = ()
    for elem in my_list:
        if elem[0]== elem[1]:
            continue
        s = 3.14*elem[0]*elem[1]
        if s > maxi:
            maxi = s
            kort = elem
    return kort

orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
print(*find_farthest_orbit(orbits))
#print(orbits, sep=' || ')  # [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
print(*orbits, sep=' || ')  # (1, 3) || (2.5, 10) || (7, 2) || (6, 6) || (4, 3)
