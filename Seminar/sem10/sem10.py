def my_funk():
    print('ddd1')


def my_funr2():
    print('sss2')


my_dict = {1: my_funk, 2: my_funr2}
n = int(input())
my_dict[n]()


