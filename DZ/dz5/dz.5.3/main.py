from comp_human import comp_hum
from human_comp import hum_comp
from human_human import hum_hum
from funk import *

if game_mode() == 1:
    print('Вы выбрали игру с ботом\n')
    if first_player_choice() == 0:
        player_one = computer_first_player()
        player_two = second_human_player()
        # print(
        #     'Поле игры крестики нолики\n и номера для заполнения\n пустых клеток')
        #board_play(board)
        comp_hum(player_one, player_two)

    else:
        player_one = first_human_player()
        player_two = computer_second_player()
        # print(
        #     'Поле игры крестики нолики\n и номера для заполнения\n пустых клеток')
        board_play(board)
        hum_comp(player_one, player_two)

else:
    print('Вы выбрали игру с человеком\n')
    # Определяем имена игроков
    if first_player_choice() == 0:
        player_one = first_human_player()
        player_two = second_human_player()
        print(
            'Поле игры крестики нолики\n и номера для заполнения\n пустых клеток')
        board_play(board)
        hum_hum(player_one, player_two)
    else:
        player_two = first_human_player()
        player_one = second_human_player()
        print(
            'Поле игры крестики нолики\n и номера для заполнения\n пустых клеток')
        board_play(board)
        hum_hum(player_one, player_two)
