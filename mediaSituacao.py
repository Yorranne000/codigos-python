nota1=float(input("Informe a primeira nota "))
nota2=float(input("Informe a segunda nota "))
média=(nota1+nota2)/2
if média >= 7.0:
    print("Aprovado.")
elif média == 4.9 or média == 6.9:
    print("Recuperação.")
else:
    print("Reprovado")
