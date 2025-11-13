#4ª Questão: Vetor / Array (Lista em Python) 

temperaturas=[28.5, 30.1, 26.9, 31.8, 27.5, 29.3, 32.0, 25.8]

media=0

for graus in temperaturas:
    if graus > 29.0:
        print("Maior que 29.0C:", graus)
        
print("Lista completa", temperaturas)