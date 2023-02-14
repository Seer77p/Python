# dz 5.3
# Создайте программу для игры в ""Крестики-нолики"".
from funk_krest import *
from funk_candies import name, game_mode, difficulty_level
# Создание, инициализация игрового поля, и его печать с навигацией
board = list(range(1, 10))
print()

# Определение типа игры (люди либо человек с ботом)
if game_mode()==1:
    print('Вы выбрали игру с ботом\n')
    if difficulty_level()==0:
        print('Вы выбрали легкий уровень\n')
        
        if first_player_choice()==0:
            player_one = first_human_player()
            print('Поле игры крестики нолики\n и номера для заполнения\n пустых клеток')
            board_play(board)
                    
                                                                                  #писать игру
            
        else:
            player_one = computer_first_player()
            print('Поле игры крестики нолики\n и номера для заполнения\n пустых клеток')
            board_play(board)
            
                                                                                    # писать игру
            
    else:
        print('Вы выбрали сложный уровень уровень\n')
        if first_player_choice() == 0:
            player_one = first_human_player()
            print('Поле игры крестики нолики\n и номера для заполнения\n пустых клеток')
            board_play(board)
                                                                                    #писать игру
        else:
            player_one = computer_first_player()
            print('Поле игры крестики нолики\n и номера для заполнения\n пустых клеток')
            board_play(board)
                                                                                    # писать игру
else:
    print('Вы выбрали игру с человеком\n')
# Определяем имена игроков
if first_player_choice()==0:
    player_one = first_human_player()
    player_two=name()
else:
    player_two = second_human_player()
    player_one=name()
print('Начнем игру:\n')
print('Поле игры крестики нолики\n и номера для заполнения\n пустых клеток')
board_play(board)
while vin(board, player_one) != player_one or vin(board, player_two) != player_two:
    #print('Первым ходит игрок:', player_one, 'и играет крестиками "x" \n')
    # Первый игрок начинает ходить
    turn_x = player_turn(player_one)
    put_board_x(turn_x, board)
    board_play(board)
    print('Введенное число отмечено на поле')
    # Проверка на выигрышь по крестикам
    if vin(board, player_one)==player_one:
        print('Игрок', player_one, 'ВЫИГРАЛ!\n')   
        break 
    # Второй игрок начинает ходить
    turn_0 = player_turn(player_two)
    put_board_0(turn_0, board)
    board_play(board)
    print('Введенное число отмечено на поле')
    # Проверка на выигрышь по ноликам
    if vin(board, player_two) == player_two:
        print('Игрок', player_two, 'ВЫИГРАЛ!\n')
        break

