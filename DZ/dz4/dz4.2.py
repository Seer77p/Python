# dz-4.2
# Задайте натуральное число N. Напишите программу,
# которая составит список простых множителей числа N.

numbers = int(input('Введите натуральное число: '))
number_list = list()
while numbers != 1:
    if numbers % 2 == 0:
        number_list.append(2)
        numbers //= 2
    elif numbers % 3 == 0:
        number_list.append(3)
        numbers //= 3
    elif numbers % 5 == 0:
        number_list.append(5)
        numbers //= 5
    elif numbers % 7 == 0:
        number_list.append(7)
        numbers //= 7
    else:
        number_list.append(numbers)
        numbers //= numbers
print('Простые множители введенного числа: ', number_list, end='')
