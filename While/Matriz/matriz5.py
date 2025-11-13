
matriz=[]
linha=(int(input("Informe quantas linhas terá sua matriz: ")))
coluna=(int(input("Informe quantas colunas terá sua matriz: ")))

for i in range (linha):   
    linha=[]
    for j in range(coluna):  
        a = int(input(f"Digite um valor para [{i}][{j}]: "))
        linha.append(a)
    matriz.append(linha)
print(matriz) 

