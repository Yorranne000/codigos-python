frutas = ("maçã", "uva", "morango","abacate")
'''for fruta in frutas:
    print(fruta)'''

#[]aparece só a fruta na posicão informada 2 (lembrando que começa do 0)
print(frutas[2])

#ordenação alfabética
frutas.sort ()

#inversão de itens da lista
frutas.reverse()

#adiciona um item no final da lista
frutas.append ("mamão")
frutas.append ("pitaya")

#inserir na posição que eu determinar
frutas.insert (0, "kiwi")

#remover 
frutas.remove ("uva")

#remove o último elemento
frutas.pop()

#tamanho da lista
len(frutas)
print(len(frutas))

#descobre a posição que estar o item informado
frutas.index(("uva"))

for i in range (0,10,2):
    print(i)