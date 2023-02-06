# dz-4.1
# Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
divider = 1
pi = 0
line = int(input('Введите длину числа ПИ после запятой: '))
for i in range(1000000):
    if i % 2 == 0:
        pi += 4/divider
    else:
        pi -= 4/divider
    divider += 2
print('Число пи = ', round((pi), line))

# Второй вариант (точнее)
pi_1 = 3
plus_minus = 1
for i in range(1, 1000000):
    pi_1 += (plus_minus*4) / ((i + i)*(i + i + 1)*(i + i + 2))
    plus_minus *= -1
print('Число пи = ', round((pi_1), line))
