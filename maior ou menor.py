'''Número1 = float(input("Digite o valor do número 1 :"))
Número2 = float(input("Digite o valor do número 2 :"))
Número3 = float(input("Digite o valor do número 3 :"))


if Número1>Número2:
   if Número1>Número3:
    print("O maior número é o ",Número1)
elif Número2<Número3:
   print("O maior número é o ", Número2)
else:
   print("O maior é o número ", Número3)
if Número1<Número2:
   if Número1<Número3:
    print("O menor número é o ", Número1)
elif Número2<Número3:
   print("O menor número é o ", Número2)
else:
   print("O menor é o número ", Número3)'''

Número1 = int(input("Digite o valor do número 1 :"))
Número2 = int(input("Digite o valor do número 2 :"))
Número3 = int(input("Digite o valor do número 3 :"))

#maior número
if Número1>Número2 and Número1 > Número3:
    print("O maior número é o ", Número1)
elif Número2> Número1 and Número2 > Número3:
    print("O maior é o ", Número2)
else:
    print("O maior número é o ", Número3)
#menor número
if Número1<Número2 and Número1 < Número3:
    print("O menor número é o ", Número1)
elif Número2< Número1 and Número2 < Número3:
    print("O menor é o ", Número2)
else:
    print("O menor número é o ", Número3)