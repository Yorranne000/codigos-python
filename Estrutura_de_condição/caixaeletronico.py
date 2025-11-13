valor_do_saque=float(input("Infome o valor do saque "))
saldo_inicial=1500.00
if valor_do_saque <= 0:
    print("Valor de saque inválido")
else:
    print("Saldo insuficiente para esta operação.")
    if (valor_do_saque==saldo_inicial) or (valor_do_saque<=saldo_inicial):
        print("Saque realizado com sucesso!")
    else: 
        print("Saldo insuficiente para esta operação..")
