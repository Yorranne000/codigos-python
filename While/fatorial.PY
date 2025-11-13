numero= int(input("Digite um número natural: "))
fatorial = numero
while numero != 1:
  fatorial *= numero-1
  numero -=1
print(f"O fatorial é {fatorial}")