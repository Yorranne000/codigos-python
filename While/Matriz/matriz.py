matriz = [[1,2,3,4],                   
          [5,6,7,8],                      
          [9,10,11,12],
          [13,14,15,16]]

#print(matriz[2][3]) #imprime a posição que eu indiquei
#matriz=[2][3] = 300 (muda o valor de um elemento na matriz)

#for i in range(len(matriz)):
    #print(matriz[i])                      << #imprime todas as linhas.

for i in range(len(matriz)):
    for j in range(len(matriz)):           #<< #imprime todos os números da lista e coluna.
        print(matriz[i][j])                #primeiro o sistema roda o j depois o i. 


