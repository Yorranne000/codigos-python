'''numero_inteiro = int(input("Informe um número inteiro entre 1 e 9: "))
#5
contador = 0

# 0 = 1 2 3 4 5
# 1 = 1 2 3 4 5
# . . .
# 4 = 1 2 3 4 5
# 5

i =1
while contador <= numero_inteiro:
    print(contador,"=", end="")
    while i <= 5:
        print(i, end=" ")
        i+=1
    contador = contador + 1
    i=1
    print()'''

num = 0
 
while num < 1 or num > 9:
    num = int(input("Digite um número inteiro de 1 a 9: ")) 
i = 1
while i <= num:
    print(str(i) * i)
    i += 1
     
        
    
