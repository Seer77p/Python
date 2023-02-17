# 5.4
# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
from funk import rle_stroka, new_stroka


stroka = 'dddddddddjjjjjjjkjkkkkkkddddddddlllllllllccmmmjjjjkkkkdddnnnnccc'

rle = rle_stroka(stroka)
print('Сжатая строка: ',rle,'\n')

new_stroka(rle)
    
