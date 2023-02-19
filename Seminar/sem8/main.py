# Создать телефонный справочник с
# возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер
# телефона - данные, которые должны находиться
# в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в
# текстовом файле
# 3. Пользователь может ввести одну из
# характеристик для поиска определенной
# записи(Например имя или фамилию
# человека)
# 4. Использование функций. Ваша программа
# не должна быть линейной

# def read_data():
#     with open('text.txt', 'r', encoding='utf-8') as file:
#         my_list = file.readlines()
#         return(my_list)
    
# def print_data(my_list):
#     for i in my_list:
#         print(i.strip())
        
# def add_user(my_list):
#     my_list.append('\n' + input("Добавьте пользователя: "))
    
# def write_data():
#     with open('text.txt', 'w', encoding='utf-8') as file:
#         file.writelines(my_list)
        
# def search_data():
#     text = input('Введите текст для поиска: ')
#     for elem in my_list:
#         if text in elem:
#             print(elem.strip())

# my_list = read_data()
# print_data(my_list)
# add_user(my_list)
# print_data(my_list)
# write_data()
# search_data()

def menu():
    pass

def change_data():
    pass

def write_data():
    pass

def read_data():
    with open('fio.txt', 'r', encoding='utf-8') as file:
        data = file.readlines()
    return data

def screen(data):
    for elem in data:
        print(elem)

def main():
    data = read_data()
    screen(data)

if __name__ == '__main__':
    main()
