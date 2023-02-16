from funk import *


def comp_hum(player_one, player_two):
    while vin_x(board, player_one) != player_one or vin_0(board, player_two) != player_two:
        put_board_computer_x(board)
        board_play(board)
        print('Введенное число отмечено на поле')
        if vin_x(board, player_one) == player_one:
            print('Игрок', player_one, 'ВЫИГРАЛ!\n')
            break
        turn_0 = player_turn(player_two)
        put_board_0(turn_0, board)
        board_play(board)
        print('Введенное число отмечено на поле')
        # Проверка на выигрышь по ноликам
        if vin_0(board, player_two) == player_two:
            print('Игрок', player_two, 'ВЫИГРАЛ!\n')
            break
    
