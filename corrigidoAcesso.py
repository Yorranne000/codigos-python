#2ª Questão: Estruturas Condicionais e Operadores Lógicos 

acesso=input("Informe seu usuário: ")
pontuacao=int(input("Digite seu nível de pontuação: "))

if acesso == "Administrador" and pontuacao > 750:
     print("Acesso Liberado.Bem-vindo(a)!")
elif acesso == "Premium" and pontuacao > 750:
    print("Acesso Liberado.Bem-vindo(a)!")
else:
    print("Nível de acesso não autorizado!")