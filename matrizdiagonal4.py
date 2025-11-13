
#diagonal
matriz=[[0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0]]

for i in range (len(matriz)):
    for j in range (len(matriz[0])):
        if i ==j:
            matriz[i][j]= 1
        else:
            matriz[i][j]
for i in range (len(matriz)):
    print(matriz[i])
