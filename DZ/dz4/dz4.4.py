# dz-4.4
# Задана натуральная степень k. Сформировать случайным
# образом список коэффициентов (значения от 0 до 100)
# многочлена и записать в файл многочлен степени k.
# Пример: - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
from random import randint

k = int(input('Введите коэффициент k: '))
my_list = list()
for i in range(k + 1):
    my_list.append(randint(1, 101))
polynomial = ''
if k < 1:
    polynomial = 'x = 0'
else:
    for i in range(k+1):
        if i != k-1 and my_list[i] != 0 and i != k:
            polynomial += f'{my_list[i]}x^{k - i}'
            if my_list[i] != 0:
                polynomial += ' + '
        elif i == k-1 and my_list[i] != 0:
            polynomial += f'{my_list[i]}x'
            if my_list[i] != 0:
                polynomial += ' + '
        elif i == k and my_list[i] != 0:
            polynomial += f'{my_list[i]} = 0\n\n'
        elif i == k and my_list[i] == 0:
            polynomial += ' = 0'
with open('dz4.5.txt', 'w') as file:
    file.write(polynomial)
print(polynomial)
