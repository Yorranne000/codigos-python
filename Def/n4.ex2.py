def dizer_ola():
    print("Olá!")
 
def calcular_media():
    n1 = float(input("Digite a primeira nota: "))
    n2 = float(input("Digite a segunda nota: "))
    media = (n1 + n2) / 2
    print(f"A média é: ",(media))
 
def menu():
    opcao = "0"  
    while opcao != "3":
        print("   MENU   ")
        print("1 - Dizer Olá")
        print("2 - Calcular Média")
        print("3 - Encerrar")
        
        opcao = input("Escolha uma opção: ")
 
        if opcao == "1":
            dizer_ola()
        elif opcao == "2":
            calcular_media()
        elif opcao == "3":
            print("Encerrando o programa! ")
        else:
            print("Opção inválida! Tente novamente.")
 
menu()