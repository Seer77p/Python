# dz 5.2
# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая
# ход друг после друга. Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""
from random import randint, random

player_bot = 'Соперник=компьютер'
count = 0
maxi=28
victory_number = 57
game_mode_selection = int(input(
    'Введите режим игры(2 человека,  введите "2", либо человек против бота "1")'))
if game_mode_selection == 1:
    print('Игра человека против бота!')

    complexity = int(input('Введите сложность 0 - легче, 1 сложнее:'))
    if complexity == 0:
        player = str(input('Введите имя игрока: '))
        candies = int(input('Введите общее количество конфет: '))
        print('Начнем игру\n')
        while 0 <= candies:
            count += 1
            if count % 2 == 0:
                print('Ход игрока', player, ': ')
                quantity = int(input('Введите количество конфет от 1 до 28: '))
            else:
                print('Ход компьютера', player_bot, ': ')
                
                if candies <= maxi:
                    quantity = randint(1, candies)
                    print('Компьютер забрал', quantity, 'конфет')
                else:
                    quantity = randint(1, maxi+1)
                    print('Компьютер забрал', quantity, 'конфет')
            if candies-quantity < 0:
                quantity = int(
                    input('Вы ввели количество больше остатка, введите не больше чем осталось:'))
            elif quantity == 0:
                quantity = int(
                    input('Вы ввели 0, введите от 1 до 28, но не больше остатка:'))
            elif candies-quantity == 0:
                if count % 2 == 0:
                    print('Игрок', player, 'выиграл')
                else:
                    print('Игрок', player_bot, 'выиграл')
                break
            else:
                candies -= quantity
                print('Вы взяли ', quantity, 'конфет', 'осталось = ', candies)

    elif complexity == 1:
        player = str(input('Введите имя игрока: '))
        candies = int(input('Введите общее количество конфет: '))
        print('Начнем игру\n')
        while 0 <= candies:
            count += 1
            if count % 2 == 0:
                print('Ход игрока', player, ': ')
                quantity = int(input('Введите количество конфет от 1 до 28: '))
            else:
                print('Ход компьютера', player_bot, ': ')
                
                if candies <= maxi:
                    quantity = candies
                    print('Компьютер забрал', quantity, 'конфет')
                else:
                    
                    if victory_number > candies:
                        quantity = victory_number-candies
                    else:
                        quantity = randint(1, maxi+1)
                    print('Компьютер забрал', quantity, 'конфет')
            if candies-quantity < 0:
                quantity = int(
                    input('Вы ввели количество больше остатка, введите не больше чем осталось:'))
            elif quantity == 0:
                quantity = int(
                    input('Вы ввели 0, введите от 1 до 28, но не больше остатка:'))
            elif candies-quantity == 0:
                if count % 2 == 0:
                    print('Игрок', player, 'выиграл')
                else:
                    print('Игрок', player_bot, 'выиграл')
                break
            else:
                candies -= quantity
                print('Вы взяли ', quantity, 'конфет', 'осталось = ', candies)


elif game_mode_selection == 2:
    player_one = str(input('Введите имя первого игрока: '))
    player_two = str(input('Введите имя второго игрока: '))
    candies = int(input('Введите общее количество конфет: '))
    print('Начнем игру\n')
    while 0 <= candies:
        count += 1
        if count % 2 == 0:
            print('Ход игрока', player_two, ': ')
            quantity = int(input('Введите количество конфет от 1 до 28: '))
        else:
            print('Ход игрока', player_one, ': ')
            quantity = int(input('Введите количество конфет от 1 до 28: '))

        if candies-quantity < 0:
            quantity = int(
                input('Вы ввели количество больше остатка, введите не больше чем осталось:'))
        elif quantity == 0:
            quantity = int(
                input('Вы ввели 0, введите от 1 до 28, но не больше остатка:'))
        elif candies-quantity == 0:
            if count % 2 == 0:
                print('Игрок', player_two, 'выиграл')
            else:
                print('Игрок', player_one, 'выиграл')
            break
        else:
            candies -= quantity
            print('Вы взяли ', quantity, 'конфет', 'осталось = ', candies)
