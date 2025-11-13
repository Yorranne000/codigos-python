matriz = [[0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]]
 
for i in range(4):
    for j in range(4):
        matriz[i][j] = int(input(f"Informe o elemento na posição [{i}][{j}]: "))
print(matriz)

#for linha in matriz:
#    print(linha)