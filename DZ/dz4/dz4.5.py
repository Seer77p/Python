# dz-4.5
# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.
print()

q="11x ^ 5 + 39x ^ 4 + 81x ^ 3 + 86x ^ 2 + 22x + 60 = 0"
polynomial_one = q.replace(" ", "").replace("^", "")
polynomial_one = polynomial_one[:-2]
poly_list_one = list(polynomial_one)
for i in range(1, len(poly_list_one)):
    if poly_list_one[i] == 'x':
        if poly_list_one[i+1] == '+':
            break
        else:
            poly_list_one.pop(i+1)
polynomial_one = ''.join(poly_list_one)
polynomial_one = polynomial_one.replace("x", "")
polynomial_one = polynomial_one.replace("+", " ")
polynomial_one = polynomial_one.split(" ")
polynomial_one.reverse()

q1 = '93x^3 + 44x^2 + 45x + 60 = 0'
polynominal_two = q1.replace(" ", "").replace("^", "")
polynominal_two = polynominal_two[:-2]
poly_list_two = list(polynominal_two)
for i in range(1, len(poly_list_two)):
    if poly_list_two[i] == 'x':
        if poly_list_two[i+1] == '+':
            break
        else:
            poly_list_two.pop(i+1)
polynominal_two = ''.join(poly_list_two)
polynominal_two = polynominal_two.replace("x", "")
polynominal_two = polynominal_two.replace("+", " ")
polynominal_two = polynominal_two.split(" ")
polynominal_two.reverse()


summ = list()
if len(polynomial_one) > len(polynominal_two):
    size = len(polynomial_one)
else:
    size = len(polynominal_two)
for i in range(size):
    if len(polynomial_one) < size:
        polynomial_one.append(0)
    elif len(polynominal_two) < size:
        polynominal_two.append(0)
    summ.append(int(polynomial_one[i])+int(polynominal_two[i]))

w = list()
for i in range(len(summ)):
    if i == 0:
        w.append(f'{summ[i]} ')
    elif i == 1:
        w.append(f'{summ[i]}x + ')
    else:
        w.append(f'{summ[i]}x^{i} + ')
w.reverse()
w = ''.join(w)
print(' Многочлен 1: ', q, '\n+\n', 'Многочлен 2: ',
      q1, '\n=\n', 'Сумма многочленов =', w, '=', '0\n')
