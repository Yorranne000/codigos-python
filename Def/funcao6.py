def teste():
    x=10    #variavel local
    print("Dentro da função: ",x)

x=5
teste()     #variavel global     
print("Fora da função: ",x)