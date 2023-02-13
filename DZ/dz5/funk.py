from random import randint

maxi = 28
victory_number = 57

def name():
    player = str(input('Имя игрока: '))
    return player

def candies_numbers():
    candies = int(input('Введите общее количество конфет: '))
    while candies == 0:
        print('Введенный размер списка', candies, 'не может быть нулевым')
        candies = int(input('Введите количество конфет: '))
    return int(candies)

def game_mode():
    game_mode_selection = int(input(
        'Введите режим игры ( 2 человека,  введите "2", либо человек против бота "1" )'))
    while 1 != game_mode_selection != 2:
        game_mode_selection = int(input('Необходимо ввести либо "1" либо "2" '))
    return game_mode_selection

def difficulty_level():
    complexity = int(input('Введите сложность 0 - легче, 1 сложнее: '))
    while 1 != complexity != 0:
        complexity = int(input('Необходимо ввести либо "1" либо "0" '))
    return complexity

def checks_number(candies):
    quantity = int(
        input('Введите число в интервале от 1 до 28(включительно) = '))
    while 1 > quantity or quantity > 28:
        print('Вы ввели число ', quantity, 'это за границами условия')
        quantity = int(input('Введите число от 1 до 28 = '))
    while (candies-quantity) < 0:
        print('Вы ввели количество больше остатка на = ', candies-quantity)
        quantity = int(
            input('Введите количество не больше чем осталось: = '))
    return quantity

def base_game_man(player_one, player_two, candies):
    count = 0
    count = randint(0, 1)
    while 0 <= candies:
        count += 1
        if count % 2 == 0:
            print('Ход игрока', player_one, ': ')
            quantity = int(checks_number(candies))
        else:
            print('Ход игрока', player_two, ': ')
            quantity = int(checks_number(candies))
        if candies-quantity == 0:
            if count % 2 == 0:
                print('\nИгрок', player_one, 'выиграл\n')
            else:
                print('\nИгрок', player_two, 'выиграл\n')
            break
        else:
            candies -= quantity
            print('Вы взяли ', quantity, 'конфет', 'осталось = ', candies)

def base_game_computer_easy(player, candies):
    player_bot = 'Соперник=компьютер'
    count = randint(0, 1)
    while 0 <= candies:
        count += 1
        if count % 2 == 0:
            print('Ход игрока', player, ': ')
            quantity = int(checks_number(candies))
        else:
            print('Ход компьютера', player_bot, ': ')
            if candies <= maxi:
                quantity = randint(1, candies)
                print('Компьютер забрал', quantity, 'конфет')
            else:
                quantity = randint(1, maxi+1)
                print('Компьютер забрал', quantity, 'конфет')

        if candies-quantity == 0:
            if count % 2 == 0:
                print('\nИгрок', player, 'выиграл\n')
            else:
                print('\nИгрок', player_bot, 'выиграл\n')
            break
        else:
            candies -= quantity
            print('Вы взяли ', quantity, 'конфет',
                  'осталось = ', candies)

def base_game_computer_difficult_level(player, candies):
    player_bot = 'Соперник=компьютер'
    count = randint(0, 1)
    while 0 <= candies:
        count += 1
        if count % 2 == 0:
            print('Ход игрока', player, ': ')
            quantity = int(checks_number(candies))
        else:
            print('Ход компьютера', player_bot, ': ')
            if candies <= maxi:
                quantity = candies
                print('Компьютер забрал', quantity, 'конфет')
            else:
                if victory_number > candies:
                    quantity = candies-(maxi+1)
                else:
                    quantity = randint(1, maxi+1)
                    print('Компьютер забрал', quantity, 'конфет')
        if candies-quantity == 0:
            if count % 2 == 0:
                print('\nИгрок', player, 'выиграл\n')
            else:
                print('\nИгрок', player_bot, 'выиграл\n')
            break
        else:
            candies -= quantity
            print('Игрок взял ', quantity, 'конфет',
                  'осталось = ', candies)


if __name__ == '__main__':  # усли в качестве импорта не будт запускаться
    print('Запускаю')
