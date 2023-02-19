

def menu(my_list):
    print('\nВыберите действие: ', '\nДобавить абонента = 1', '\nУдалить значение = 2',
          '\nРедактировать справочник = 3', '\nНайти абонента = 4', '\nРаспечатать справочник = 5')

    temp = int(input())
    if temp == 1:
        add_data(my_list)  # Добавить

    elif temp == 2:
        removal(my_list)

        # Удалить
    elif temp == 3:
        correct(my_list)

        # Исправить
    elif temp == 4:
        search(my_list)

        # Найти
    elif temp == 5:
        print_data(my_list)

    return my_list
    # Печать kdj


def removal(my_list):
    my_new_list = list()
    name = input(
        'Введите имя, фамилию, отчество, номер телефона по которому будет осуществляться поиск данных абонента для удаления: ')
    for i in my_list:
        if name in i:
            print('Удаляемая ячейка: ', i)
        else:
            my_new_list.append(i)
    print(my_new_list)
    my_list = my_new_list
    write_data(my_list)
    return my_list


def search(my_list):
    name = input(
        'Введите имя, фамилию, отчество, номер телефона по которому будет осуществляться поиск: ')
    for i in my_list:
        if name in i:
            print('\nИскомый абонент : ', i)


def correct(my_list):
    my_new_list = list()
    new = ''
    print('Введите имя, фамилию, отчество, номер телефона по которому будет осуществляться поиск данных абонента для редактирования: ')
    name = str(input())
    for i in my_list:
        if name in i:
            print('Искомая для исправления ячейка: ', i)
            new = input('\nВнесите исправления: ')
        else:
            my_new_list.append(i)
    my_new_list.append('\n'+new)
    print(my_list)
    my_list = "".join(my_new_list)
    print(my_list)
    write_data(my_list)
    return my_list


def write_data(my_list):
    with open('fio.txt', 'w', encoding='utf-8') as file:
        my_list = "".join(my_list)
        file.write(my_list)


def read_data():
    with open('fio.txt', 'r', encoding='utf-8') as file:
        my_list = list(file.readlines())
        print(my_list)
    return my_list


def add_data(my_list):
    my_list.append('\n' + input("\nДобавьте абонента: "))
    write_data(my_list)
    print(my_list)
    return my_list


def print_data(my_list):
    for elem in my_list:
        print(elem)


def main():
    My_list = read_data()
    print_data(My_list)
    menu(My_list)


if __name__ == '__main__':
    main()
