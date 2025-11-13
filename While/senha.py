senha = ()
while senha != "senac123":
    senha = input("Digite a senha: ")
    if senha != "senac123":
        print("Senha incorreta! Tente novamente.")
    else:
        print("Acesso permitido!")