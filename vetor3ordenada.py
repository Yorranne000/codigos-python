vetor=[4,3,2,1]
print("Desordenado", vetor)

for i in range (len(vetor)-1): #Este-1 simboliza os passos que vai dar. Para calcular é só `pegar` a quantidade da lista(vetor) menos 1. (pra essa lista=4-1=3 passos)
    for j  in range (len(vetor)-1-i): #esse i é a quantidade de numeros que estou checando para trocar. i é o giro do elemento da lista.
        if vetor[j+1]< vetor[j]:  #+1 é o sucessor
            temp = vetor[j]        #temp = minha variavel temporária para guardar o primeiro numero da lista.
            vetor[j]=vetor[j+1]
            vetor[j+1] = temp

print("Ordenado", vetor)