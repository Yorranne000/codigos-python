nomes = ["Davi", "Maria", "Kelvin"]
a=0
e=0

for nome in nomes:
    for letra in nome:
        if letra == "a":
            a+=1
        elif letra == "e":
            e+=1
    print(f"O nome {nome} possui {a} 'a' e {e} 'e'")    
    a=0
    e=0

#esse a=0 e e=0 no final é usado para reiniciar a contagem para o próximo nome.

   