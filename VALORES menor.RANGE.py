valores = []

for i in range(1,11,1):  
    valores.append(int(input(f"Digite o {i} valor: ")))   
menor = valores[0]

for i in range(len(valores)):
    if valores[i] < menor:
        menor = valores[i]

print(len(valores))
print(f"O menor valor é: {menor}")
