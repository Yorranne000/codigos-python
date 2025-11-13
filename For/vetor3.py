nomes= []
nota1=[]
nota2=[]
media= []
situacao=[]

for i in range(6):
    nomes.append(input("Informe seu nome:"))
    nota1.append(float(input("Informe sua primeira nota:")))
    nota2.append(float(input("Informe sua segunda nota:")))
    media.append((nota1[i]+nota2[i])/2)
    if media [i] >=5:
        situacao.append("Aprovado!")
    else:
        situacao.append("Reprovado!")
print(nomes), print(media), print(situacao)



