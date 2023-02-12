def name():
    player = str(input('Имя игрока:'))
    return player


def candies_numbers():
    candies = int(input('Введите общее количество конфет: '))
    while candies == 0:
        print('Введенный размер списка', candies, 'не может быть нулевым')
        candies = int(input('Введите размер списка: '))
    return int(candies)


def game_mode():
    game_mode_selection = int(input(
        'Введите режим игры (2 человека,  введите "2", либо человек против бота "1")'))
    while 1 != game_mode_selection != 2:
        game_mode_selection = int(input('Необходимо ввести либо "1" либо "2"'))
    return game_mode_selection

def difficulty_level():
    complexity = int(input('Введите сложность 0 - легче, 1 сложнее:'))
    while 1 != complexity != 0:
        complexity = int(input('Необходимо ввести либо "1" либо "0"'))
    return complexity




if __name__ == '__main__':  # усли в качестве импорта не будт запускаться
    print('Запускаю')
