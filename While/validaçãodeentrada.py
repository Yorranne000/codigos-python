nota = float(input("Informe uma nota de 0 a 10: "))


if nota > 10 or nota <0:
    print("Nota inválida. Informar um número de 0 a 10")
    nova_nota = float(input("Informe uma nota de 0 a 10: "))

    while nova_nota > 10 or nova_nota < 0:
        print("Nota inválida. Informar um número de 0 a 10")
        nova_nota = float(input("Informe uma nota de 0 a 10: "))

if nova_nota >= 10:
    print("Nota válida")
else:
    print("Nota válida")
