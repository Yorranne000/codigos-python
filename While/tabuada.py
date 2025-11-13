'''tabuada = int(input("Digite o número da tabuada: "))
 
for i in range(1,11):
    print(f"{tabuada} * {i} = {tabuada * i}")'''


tabuada = int(input("Digite o número da tabuada: "))
n= 1
resultado=0

while n<=10:
   resultado=tabuada*n
   print(f"O resultado é: {tabuada} * {n} = {resultado}")
   n+=1



