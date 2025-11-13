Idade=int(input("Informe a sua idade ."))

if Idade > 0 or Idade <= 12:
    print("Criança")
elif Idade >= 13 and Idade <= 17:
    print("Adolescente")
elif Idade >= 18 and Idade <=25:
    print("Adulto Jovem")
elif Idade > 25 and Idade <=59:
    print("Adulto Pleno")
elif Idade >= 60:
    print("Idoso")
if Idade < 0:
     print("Idade inválida, insira um valor positivo")