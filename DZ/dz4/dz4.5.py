# dz-4.5
# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.
# a=[1,2,3,4,5,6,7,8,9,10,11]
# b=a[::-1]
# #c=str(a^b)
# if b==chr(94):
#     print(b)
# print(b,chr(94))
# print(ord('^'))
# print(chr(42))

import re

q = "11x ^ 5 + 39x ^ 4 - 81x ^ 3 + 86x ^ 2 + 22x + 60 = 0"

q1 = q.replace(" ", "").replace("^", "")
q1 = q1[:-2]
# q_list = q[::-1]
qpl = list()
qlist = list(q1)
print(qlist, '\n', len(qlist), '\n')

for i in range(len(qlist)):
    if (qlist[i] == "+") or (qlist[i] == "-"):
        # if qlist[i-1] != 'x':
        #     print(i-1, end='')
        #     qlist.pop(i-1)


#print(q1, '\n', qlist)