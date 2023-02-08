#dz-4.5
# Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.
a=[1,2,3,4,5,6,7,8,9,10,11]
b=a[::-1]
#c=str(a^b)
if b==chr(94):
    print(b)
print(b,chr(94))
print(ord('^'))
print(chr(42))

import re

q="11x ^ 5 + 39x ^ 4 - 81x ^ 3 + 86x ^ 2 + 22x + 60 = 0"
#q="123+ 321- 456+554- 587 +6587 -854"
#q=q.replace(" ", "")
k=0
wplus=q.split('+')

# for i in range(len(q)):
#     if q[i]=='+':
#         k=q[i-1]
#         wplus=q[i]
print(wplus, end='')  

