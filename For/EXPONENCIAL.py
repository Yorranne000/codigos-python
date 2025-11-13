x = int(input("Informe o valor de X: "))
y = int(input("Informe o valor de Y: "))


resultado = x

for i in range(y-1):
   resultado = resultado * x
print(resultado)