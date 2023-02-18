from funk import calc, random_ini, index

number_one=int(input('Введите первое число прогрессии = \n'))
step=int(input('Введите шаг(разность) прогрессии = \n'))
size=int(input('Введите размер прогрессии(до какого элемента) = \n'))

print(calc(number_one, step, size))



maxi = int(input('Введите максимальное число: '))
mini = int(input('Введите минимальное число: '))
size_2 = int(input('Введите количество чисел: '))
my_list = random_ini(size_2)
print(my_list)

my_list2 = index(my_list, maxi, mini)
print('\nМаксимальное число = ',maxi,'\nМинимальное число = ',mini, 
      '\nИндексы элементов, входящие диапозон от "',maxi,'" до "', mini,'"', my_list2)
