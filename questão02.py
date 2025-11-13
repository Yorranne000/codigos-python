#2ª Questão: Estruturas Condicionais e Operadores Lógicos 

acesso=input("Informe seu usuário: ")
pontuacao=int(input("Digite seu nível de pontuação: "))

if acesso == "Administrador" and "Premium" or pontuacao > 750:
    print("Acesso Liberado.Bem-vindo(a)!")
elif pontuacao <= 750:
    print("Acesso negado. Pontuação insuficiente!")
else:
    print("Nível de acesso não autorizado!")