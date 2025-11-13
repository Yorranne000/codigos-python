matriz = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12],
          [13, 14, 15, 16]]

contador = 0

for i in range(len(matriz)):
    for j in range(len(matriz)):
        if matriz[i][j] > 10:
            contador+=1
print("A matriz possui", contador, "valores maiores que 10.")
        



    
        
    
  