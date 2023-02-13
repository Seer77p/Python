#dz 5.3
#Создайте программу для игры в ""Крестики-нолики"".
size=3
playing_field=[[1,2,3],[4,5,6],[7,8,9]]
for i in range(0, len(playing_field)):
    for j in range(0, len(playing_field)):
        print(playing_field[i][j], end='  ')
    print()
    
print(playing_field)
    
