 #verificar se a palavra é um palíndromo 
frase = input("Digite uma palavra ou uma frase: ")

#remove os espaços
sem_espaco = ""
for letra in frase:
    if letra != " ":
        sem_espaco += letra

#variável para contar as diferenças
erros = 0

#compara as letras da frente e de trás pra frente
for i in range(len(sem_espaco)):
    if sem_espaco[i] != sem_espaco[len(sem_espaco) - 1 - i]:
        erros += 1

#se não der erro, é palíndromo
if erros == 0:
    print("É um palíndromo!")
else:
    print("Não é um palíndromo.")
