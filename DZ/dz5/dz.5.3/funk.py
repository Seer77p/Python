from random import randint


player_one = 0
player_two = 0
player_bot = 'Соперник=компьютер'

board = list(range(1, 10))
print()

def name():
    player = str(input('Имя игрока: '))
    return player

def board_play(board):
    size = 3
    print('           ', '-'*13)
    for i in range(size):
        print('            |', board[0+i*3], '|',
              board[1+i*3], '|', board[2+i*3], '|')
        print('            ', '-'*13)

def game_mode():
    game_mode_selection = int(input(
        'Введите режим игры ( 2 человека,  введите "2", либо человек против бота "1" )'))
    while 1 != game_mode_selection != 2:
        game_mode_selection = int(
            input('Необходимо ввести либо "1" либо "2" '))
    return game_mode_selection

def first_player_choice():
    temp = 0
    temp = randint(0, 1)
    return temp

def first_human_player():
    player_one = name()
    print('Игрок', player_one, ' ходит первым\n')
    print('Начнем игру:\n')
    return player_one

def second_human_player():
    player_two = name()
    print('Игрок', player_two, ' ходит вторым')
    return player_two


def computer_first_player():
    print('Компьютер ходит первым\n')
    player_one = player_bot
    print('Начнем игру:\n')
    return player_one


def computer_second_player():
    print('Компьютер ходит вторым\n')
    player_two = player_bot
    return player_two


def player_turn(player):
    turn = 0
    print('Игрок', player, 'введите номер ячейки для вашего хода: ', end='')
    turn = int(input())
    while 1 > turn or turn > 9:
        print('Вы ввели число не соответствуещее имеющимся позициям')
        turn = int(input('Введите число от "1" до "9" (включительно): '))
    return turn


def put_board_x(turn_x, board):
    while board[turn_x-1] == 'x' or board[turn_x-1] == '0':
        turn_x = int(input('Ячейка занята, введите другую: '))
    if board[turn_x-1] == turn_x:
            board[turn_x-1] = 'x'


def put_board_0(turn_0, board):
    while board[turn_0-1] == 'x' or board[turn_0-1] == '0':
        turn_0 = int(input('Ячейка занята, введите другую: '))
    if board[turn_0-1] == turn_0:
        board[turn_0-1] = '0'


def put_board_computer_0(board):
    turn_computer_0 = 1
    while board[turn_computer_0-1] == 'x' or board[turn_computer_0-1] == '0':
        turn_computer_0 = randint(1, 9)
    if board[turn_computer_0-1] == turn_computer_0:
        board[turn_computer_0-1] = '0'


def put_board_computer_x(board):
    turn_computer_x = 1
    while (board[turn_computer_x-1] == 'x') or (board[turn_computer_x-1] == '0'):
        turn_computer_x = randint(1, 9)
    if board[turn_computer_x-1] == turn_computer_x:
        board[turn_computer_x-1] = 'x'
        

def vin_x(board, player_one):
    for i in range(3):
        if (board[0+i*3] == board[1+i*3] == board[2+i*3] == 'x'):
            return player_one
        if (board[0+i] == board[3+i] == board[6+i] == 'x'):
            return player_one
    if (board[0] == board[4] == board[8] == 'x'):
        return player_one
    if (board[6] == board[4] == board[2] == 'x'):
        return player_one
    
    
    
def vin_0(board, player_two):
    for i in range(3):
        if (board[0+i*3] == board[1+i*3] == board[2+i*3] == '0'):
            return player_two
        if (board[0+i] == board[3+i] == board[6+i] == '0'):
            return player_two
    if (board[0] == board[4] == board[8] == '0'):
        return player_two
    if (board[6] == board[4] == board[2] == '0'):
        return player_two





    
