# pip freeze > requiremennts.txt
# my_list = [1, 4, 6, 8, 4, 3]

# max_elem = 0
# for i in range(6):
#     if my_list[i] > max_elem:
#         max_elem = my_list[i]
#     print(my_list[i])
# print(max_elem)
# print(max(my_list)) #8
# print(min(my_list)) #1
# print(sum(my_list)) #26
# print(sum(my_list)/len(my_list))

# my_list=[]
# for i in range(10):
#     my_list.append(i*i)
# print (my_list)

# my_list=[1, 4, 9, 40,'htllo', 40, 'abba']
# stroki=[] # так же =list() создает список пустой
# chisla=[]
# for elem in my_list:
#     if type(elem)==int:
#         chisla.append(elem)
#     else:
#         stroki.append(elem)
# print(stroki)
# print(chisla)
# print(my_list.count(40)) # Количество 40 ищет
# my_tuple=(1, 4, 9, 'hello') кортеж нельзя изменить размер, елементы

# Словарь
# my_dict = {'cat': 'Кошка', 'dog': 'Собака', 1: 'number'}
# my_dict['new'] = 'новый'
# print(my_dict['cat' 'dog' 1])

# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6
# Примечание: Пользователь может вводить значения
# списка или список задан изначально.
# inputList = [1, 1, 2, 0, -1, 3, 4, 4]
# print(inputList)
# print(len(set(inputList)))


# inputList = [1, 1, 2, 0, -1, 3, 4, 4]
# print(inputList)
# сountList = []
# for i in inputList:
#         if i not in countList:
#             countList.append(i)
# print(inputList)
# print(len(countList))



# Дана последовательность из N целых чисел и число
# K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K –
# положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]
# Примечание: Пользователь может вводить значения
# списка или список задан изначально.
# spisok = [1, 2, 3, 4, 5]
# number = 3
# slice_spisok1 = spisok[number:]
# slice_spisok2 = spisok[:number]
# result_spisok = slice_spisok1 + slice_spisok2
# print(result_spisok)

