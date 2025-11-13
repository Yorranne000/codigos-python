numero_secreto=7

int(input("Advinhe qual é o número secreto: "))

while numero_secreto < 7:         
    int(input("Advinhe qual é o número secreto: "))
print("Tente um número maior!")
int(input("Advinhe qual é o número secreto: "))

if numero_secreto > 7:         
    int(input("Advinhe qual é o número secreto: "))
print("Tente um número menor!")
int(input("Advinhe qual é o número secreto: "))
if numero_secreto == 7:
    print("Você acertou o número secreto!", numero_secreto)


