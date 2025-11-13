valor_inteiro=int(input("Digite um valor inteiro: "))
print(str(valor_inteiro))

notas_100 = valor_inteiro // 100
valor_inteiro %= 100

notas_50 = valor_inteiro // 50
valor_inteiro = valor_inteiro % 50

notas_20 = valor_inteiro // 20
valor_inteiro = valor_inteiro % 20

notas_10 = valor_inteiro // 10
valor_inteiro = valor_inteiro % 10

notas_5 = valor_inteiro // 5
valor_inteiro = valor_inteiro % 5

notas_2 = valor_inteiro // 2
valor_inteiro = valor_inteiro % 2

notas_1 = valor_inteiro // 1

#Resultado

print(str(notas_100) + "notas de 100.00")
print(str(notas_50) + "notas de 50.00")
print(str(notas_20) + "notas de 20.00")
print(str(notas_10) + "notas de 10.00")
print(str(notas_5) + "notas de 5.00")
print(str(notas_2) + "notas de 2.00")
print(str(notas_1) + "notas de 1.00")

