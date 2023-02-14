# функции крестики - нолики
from random import randint
from funk_candies import name
def board_play(board):
    size = 3
    # print('Поле игры крестики нолики\n и номера для заполнения\n      пустых клеток')
    print('           ', '-'*13)
    for i in range(size):
        print('            |', board[0+i*3], '|',
              board[1+i*3], '|', board[2+i*3], '|')
        print('            ', '-'*13)


def player_turn(player):
    turn = 0
    print('Игрок', player, 'введите номер ячейки для вашего хода: ', end='')
    turn = int(input())
    while 1 > turn or turn > 9:
        print('Вы ввели число не соответствуещее имеющимся позициям')
        turn = int(input('Введите число от "1" до "9" (включительно): '))

    return turn


def put_board_x(turn, board):
    while board[turn-1] == 'x' or board[turn-1] == '0':
        turn=int(input('Ячейка занята, введите другую: '))
    if board[turn-1] == turn:
        board[turn-1] = 'x'
    

def put_board_0(turn, board):
    while board[turn-1] == 'x' or board[turn-1] == '0':
        turn = int(input('Ячейка занята, введите другую: '))
    if board[turn-1] == turn:
        board[turn-1] = '0'


def vin(board, player_one=None, player_two=None):
    for i in range(3):
        if (board[0+i*3] == board[1+i*3] == board[2+i*3] == 'x'):
            return player_one
        if (board[0+i*3] == board[1+i*3] == board[2+i*3] == '0'):
            return player_two
        if (board[0+i] == board[3+i] == board[6+i] == 'x'):
            return player_one
        if (board[0+i] == board[3+i] == board[6+i] == '0'):
            return player_two
    if (board[0]==board[4]==board[8]=='x'):
        return player_one
    if (board[0]==board[4]==board[8]=='0'):
        return player_two
    if (board[6]==board[4]==board[2]=='x'):
        return player_one
    if (board[6] == board[4] == board[2] == '0'):
        return player_two

def first_player_choice():
    temp=0
    temp=randint(0,1)
    return temp   

player_one=0
def first_human_player():
    player_one=name()
    print('Игрок', player_one, ' ходит первым')
    return player_one

player_two=0
def second_human_player():
    player_two = name()
    print('Игрок', player_two, ' ходит первым')
    return player_two


def computer_first_player():
    player_bot = 'Соперник=компьютер'
    print('Компьютер ходит первым')
    player_one = player_bot 
    print('Начнем игру:\n')
    return player_one



if __name__ == '__main__':  # усли в качестве импорта не будт запускаться
    print('Запускаю')
