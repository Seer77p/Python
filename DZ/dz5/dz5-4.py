# 5.4
#Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

stroka='dddddddddjjjjjjjkjkkkkkkdddddddddddddlllllllllllccm'
stroka_list=list()
#stroka_list = stroka.split()
print(stroka_list)
cout=1
for i in range(1, len(stroka)):
    if stroka[i]==stroka[i-1]:
        cout+=1
        stroka_list.append(cout)
        stroka_list