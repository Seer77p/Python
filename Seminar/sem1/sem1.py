# print('hello', end='\n' 'ля ля ля')
# print('дада нет нет\nдосвидос')
# a=int(input('Введите число а= '))
# b=int(input('Введите число b= '))
# c=a+b
# print(type(c), '\n', 'Сумма a + b =', c)

# if a>b:
#     print (b)
# elif a==b:
#     print(c)
# else:
#     print(a)

# За день машина проезжает n километров. Сколько
# дней нужно, чтобы проехать маршрут длиной m
# километров? При решении этой задачи нельзя
# пользоваться условной инструкцией if и циклами.
# Input:
# n = 700
# m = 750
# Output: 2
# вариант 1
#n = int(input('Введите n: '))
# m = int(input('Введите m: '))
# d = (m + n - 1) // n
# print(d)

# вариант 2
# n = int(input('Скорость в день: '))
# m = int(input('Расстояние км: '))
# t = m//n
# ostatok = (m % n) > 0
# ostatokBool = bool(ostatok)
# ostatokDays = int(ostatok)
# print('Дней ', t + ostatokDays)

# вариант3 не всегда работает правильно 700 700 дает ошибку
# a = 700
# b = 750
# print(round(b / a + 0.5))