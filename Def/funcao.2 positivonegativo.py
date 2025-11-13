def verificar (numero):
    if numero>0:
        return("O número é positivo")
    elif numero<0:
        return("O número é negativo")
    else:
        return("Neutro")

print(verificar(int(input("Informe um número:"))))
       


