saldo = 3000
def ver_saldo(saldo):   
    print("Ver saldo", saldo)

def Deposito(saldo):
    valor_depósito = float(input("Qual valor você deseja depositar?  "))
    saldo+=valor_depósito     
    print(f"Seu depósito de {valor_depósito} foi concluído!")

def sacar(saldo):
    saque = float(input("Qual valor você deseja sacar?  "))
    saldo-=saque
    print(f"Seu saque de {saque} foi concluído!")

def menu():
    opcao = "0" 

    while opcao != "4":
        print("   MENU   ")
        print("1 - Ver saldo")
        print("2 - Depositar")
        print("3 - Sacar")
        print("4 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            ver_saldo(saldo)
        elif opcao == "2":
            Deposito(saldo)           
        elif opcao == "3":
            sacar(saldo)
        elif opcao == "4":
            print("Saindo do sistema!")
        else:
            print("Opção inválida! Tente novamente.") 
menu()