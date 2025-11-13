# ALGORITMO DE ORDENAÇÃO - MÉTODO BUBBLE SORT 
# Objetivo: Criar uma função de ordenação própria sem usar sort() ou sorted()

#LISTA INICIAL
#lista de números inteiros desordenados.

lista = [9, 18, 20, 19, 22, 3, 7, 1, 8, 5, 2, 6, 23, 25, 4, 10, 12, 11, 24, 17, 13, 15, 14]

# Exibe a lista original (antes da ordenação)
print("Lista original (desordenada):")
print(lista)

# FUNÇÃO DE ORDENAÇÃO (BUBBLE SORT)
# Essa função percorre a lista várias vezes e compara os elementos.
# Se o número da esquerda for maior que o da direita, eles trocam de lugar.

def bubble_sort(lista):
    # a variável n armazena o tamanho (quantidade de elementos) da lista
    n = len(lista)
    
    # a variável i começa em 0 e controla quantas passagens já foram feitas
    i = 0
    while i < n - 1:  # o loop roda até o penúltimo elemento
        # j é o índice usado para comparar elementos lado a lado
        j = 0
        while j < n - i - 1:
            # IF: compara dois números vizinhos
            if lista[j] > lista[j + 1]:
                # Se estiverem fora de ordem, troca de posição
                temp = lista[j]              # variável temporária para guardar o valor
                lista[j] = lista[j + 1]      # move o menor número para a esquerda
                lista[j + 1] = temp          # coloca o maior número à direita
            # aumenta o índice j para comparar o próximo par
            j += 1
        
        # aumenta o contador i (uma passagem concluída)
        i += 1
    
    # retorna a lista já ordenada
    return lista

# CHAMADA DA FUNÇÃO E EXIBIÇÃO FINAL
# o print n\ pula uma linha pra deixar visualmente mais bonito.
lista_ordenada = bubble_sort(lista)

# Mostra a lista organizada em ordem crescente
print("\nLista ordenada em ordem crescente:")
print(lista_ordenada)