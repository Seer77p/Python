# file = open('sem8.txt', 'r', encoding='utf-8')
# #text = file.read()  # считать полностью текст
# stroka1 = file.readline() # считать по строчно - строка 1
# stroka2 = file.readlines() # считать по строчно - ['строка 2\n', '\n', 'лялляяяля\n', '\n', 'ррррнпо999\n', '\n', '000']
# #print(text)
# print('dd', stroka1)
# print('ss', stroka2)
# file.close()

# file = open('sem8.txt', 'r', encoding='utf-8')
# for stroki in file:
#     print(stroki.strip(),end=' ')
# file.close()

# with open('sem8.txt', 'r', encoding='utf-8') as file:
#     for stroki in file:
#         print(stroki.strip(),end=' ') #with что бы не открывать и не закрывать
#         file.read()
#     print('ss')

# my_list=['hello\n', 'bye\n', 'ggg']
# my_list1=[1,2,3,4,5]
# my_list1=list(map(str,my_list1))
# with open('sem8.2.txt', 'w', encoding='utf-8') as file:
#     file.write('hihi\n')
#     file.write('bye-bye\n')
#     file.writelines(my_list)
 
# import os
# print(os.getcwd()) #показывает в какой директории D:\Seer77p\Python\Seminar\sem8

# import os
# import os.path
# # cur_dir=os.getcwd()
# # ld=os.listdir(cur_dir)
# # print(ld) #['main.py', 'sem8.1.txt', 'sem8.2.txt', 'sem8.py', 'sem8.txt']

# cur_dir=os.getcwd()
# if os.path.exists('sem8.2.txt'):
#     print('yes')
#     print(os.path.isdir(cur_dir+'/1'))
# my_list=list(os.walk(cur_dir)) #[('D:\\Seer77p\\Python\\Seminar
#                                 #\\sem8', [], 
#                                # ['main.py', 'sem8.1.txt', 
#                                # 'sem8.2.txt'
#                                # , 'sem8.py', 'sem8.txt'])]
# print(my_list)

# import shutil


