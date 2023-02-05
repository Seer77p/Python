# pip freeze > requiremennts.txt
# st = 'hello-my-@friend'
# my_list=st.split('@')
# print(my_list)
# my_list.sort()
# print(my_list)

# a=100
# if isinstance(a, int): #если int то выводит
#     print('int')

# st='hello'
# my_list=list(st)
# print(my_list) #['h', 'e', 'l', 'l', 'o']

# a=[0]*5
# print(a)   #[0, 0, 0, 0, 0]

# библиотека colections

# st='a'*50
# print(st)


# Множества
# my_set = {5, 7, 9}
# if 5 in my_set:
#     print('yes')

# a = [2, 4, 6, 30, 2, 6, 7, 1]
# my_set=set(a)
# print(my_set)
# new_list=list(my_set)
# print(new_list)

# my_set={5,7,9}
# my_set.add(14)
# my_set.remove(7)
# print(my_set)

# a = {1, 2, 3, 6, 5, 4}
# print(len(a))

# s=5
# print(id(s))
# b=5
# s=7
# print(id(b))
# print(id(s))
# print(s is b)

# a = [1, 3, 5]
# print(id(sum))
# sum=0
# print(id(sum))

# list comprehension
# a=[]
# for i in range(10):
#     a.append(i)

# a=[i for i in range(10)] #Будет быстрее чем выше
# print(a)

# a = [i for i in range(100) if i % 2 == 0]  # четные числа
# print(a)

# b = [i for i in a if i % 3 == 0]  # делятся на 3
# print(b)

# с = [(i, i*i) for i in a if i % 3 == 0]  # кортежи делятся на 3
# print(с)

# d = [(i, i*i) for i in a if i % 3 == 0 and i % 5 == 0]  # кортежи делятся на 3
# print(d)

# f = [(i, i*i) for i in a if i % 3 == 0]  # кортежи делятся на 3
# print(f)

# my_dict={i: i**2 for i in range(10)} #Быстрее работает
# print(my_dict)

# python -m cProfile -s time prof.py(имя файла который проверяем) 10001


# Пользователь вводит текст(строка). Словом считается
# последовательность непробельных символов идущих
# подряд, слова разделены одним или большим числом
# пробелов. Определите, сколько различных слов
# содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells
# that she sells are sea shells I'm sure. So if she sells sea
# shells on the sea shore I'm sure that the shells are sea
# shore shells
# Output: 13

myText = "She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure. So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells"
myText = myText.replace(".", "").replace(",", "").replace("!", "").replace("?", "")
myText = myText.lower()
mylist = len(set(myText.split(" ")))

print(mylist)