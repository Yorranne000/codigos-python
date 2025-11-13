Idade=int(input("Informe sua idade "))
if Idade >= 18 and Idade <= 69:
    print("Obrigatório.")
elif Idade > 15 and Idade < 18 or Idade >= 70:
    print("Opcional.")
else:
    print("Não pode votar")    
