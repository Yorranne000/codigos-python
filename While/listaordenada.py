#Fazer uma lista ordenada depois ordená-la
# Lista desordenada
#Variavél lista expõe a lista desordenada 
lista = [9, 18, 20, 19, 22, 3, 7, 1, 8, 5, 2, 6, 23, 25, 4, 10, 12, 11, 24, 17, 13, 15, 14]

print("Lista original:")
print(lista)

# Começo do algoritmo
n = len(lista)  # a variável n guarda o tamanho da lista
i = 0           #a variável i contador do laço 
#a variável j é o índice (ou posição) que indica qual elemento da lista está sendo comparado naquele momento
#exemplo: j = 0 → compara 5 e 3 → troca fica [3, 5]

while i < n - 1:
    j = 0
    while j < n - i - 1:
        # compara dois números vizinhos
        if lista[j] > lista[j + 1]:
            # troca de posição
            lista[j], lista[j + 1] = lista[j + 1], lista[j]
        j += 1
    i += 1

print("\nLista ordenada:")
print(lista)

#O n\ no começo do print pula uma linha, deixando visualmente mais bonito na hora de mostrar.