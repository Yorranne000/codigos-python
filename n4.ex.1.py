senha = (input("Digite uma senha,com 1 letra maiúscula e pelo menos 1 número: "))
maiusculo = 0
numero=0

while maiusculo == 0 or numero ==0:
    for caractere in senha:
        if caractere >= "A" and caractere <= "Z":
            maiusculo+=1
        if caractere >="0" and caractere <="9":
            numero+=1
    if maiusculo == 0 or numero ==0:
        senha = (input("Digite uma senha novamente,com 1 letra maiúscula e pelo menos 1 número: "))
print("Senha Validada!")

#