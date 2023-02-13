# dz 5.2
# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая
# ход друг после друга. Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""
from random import randint
from funk import *


game_mode_selection = int(game_mode())
if game_mode_selection == 1:
    print('Игра человека против бота!')
    complexity = int(difficulty_level())
    if complexity == 0:
        player = name()
        candies = int(candies_numbers())
        print('Начнем игру\n')
        base_game_computer_easy(player, candies)
    elif complexity == 1:
        player = name()
        candies = int(candies_numbers())
        print('Начнем игру\n')
        base_game_computer_difficult_level(player, candies)
elif game_mode_selection == 2:
    player_one = name()
    player_two = name()
    candies = int(candies_numbers())
    print('Начнем игру\n')
    base_game_man(player_one, player_two, candies)
