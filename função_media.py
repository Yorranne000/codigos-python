def calcular_media(n1,n2):
    return(n1+n2)/2
def verificar__aprovacao(media):
    if media >=7:
        return "Aprovado"
    else:
        return "Reprovado"

#n1 = int(input("Valor 1: "))
#n2 = int(input("Valor 2: "))

#media = calcular_media (n1,n2)
media = calcular_media(int(input("Valor 1: ")),int(input("Valor 2: ")))
print(verificar__aprovacao(media))
