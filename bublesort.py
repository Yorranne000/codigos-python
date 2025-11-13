#desordenada
lista = [7, 6, 4, 3]

'''
loop aninhado
lista = [7, 6, 4, 3]

for i
i = 0
for j
j = 0

i = 1 = [6, 4, 3, 7]

se lista[j] > lista[j+1]
7 > 3
temp = lista[j]
lista[j] = lista[j+1]
lista[j+1] = temp

j = 3
'''
print("Desordenada", lista)

for giro in range (len(lista)):
    for indice in range (len(lista)-giro-1):
        if lista[indice] > lista[indice+1]:
            temp = lista[indice]
            lista[indice] = lista[indice+1]
            lista[indice+1] = temp

print("Ordenada", lista)