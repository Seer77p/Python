#dz 5.3
#Создайте программу для игры в ""Крестики-нолики"".
from random import randint
from funk import *

board=list(range(1,10))  
print()  
board_play(board)

player_one = name()
player_two = name()

temp=0
temp=sequence(temp) 
if temp==0:
    print('Первым ходит игрок:', player_one,'и играет крестиками "x" ')
else:
    print('Первым ходит игрок:', player_two,'и играет ноликами "0" ')

