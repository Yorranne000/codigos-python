#PA = termo + razao e #PG RAZÃO * TERMO
#i é o contador de passos

tipo = input("Informe o tipo da progressão. Se aritimética digite PA se geométrica digite PG: ")
termo = int(input("Informe o termo da progressão: "))
razao = int(input("Informe a razão da progressão: "))
quantidade = int(input("Informe a quantidade: "))


i = 0        
while quantidade > i:
    print(termo) 
    if tipo == "PA" or tipo == "pa":
        termo +=razao
    elif tipo == "PG" or tipo == "pg":
         termo *= razao
    i+=1    

     
            