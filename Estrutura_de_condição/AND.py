#Validação de Login
usuario = input("informe o nome do usuário: ")
senha = input("informe a senha: ")

if senha == "12345" and usuario == "adimin":
    print("Acesso Concedido.")
else:
    print("Acesso Negado.")
