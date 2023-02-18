# from simple_functions import examination
from random import randint


def calc(number_one, step, size):
    result = list()
    for i in range(1, size//step+1):
        result.append(number_one+(i-1)*step)
    return result


def random_ini(size_2):
    my_list = []
    for i in range(size_2):
        my_list.append(randint(0, 100))
    return my_list


def index(my_list, maxi, mini):
    my_list2=list()
    for i in range(len(my_list)):
        if mini < my_list[i] < maxi:
            my_list2.append(int(i))
    return my_list2
