#Fibonacci (soma do Número com seus dois antecessores)

N = int(input("Informe o número: "))
F1 = 0
F2 = 1
contador = 0

#N_ésimo= F1+F2
#soma = (N-2)+(N+1) (Cálculo para somar os 2 antecessores)
#F1=F2 ?

while contador < N:
    print(F1)
    N_ésimo = F1+F2
    F1=F2 
    F2= N_ésimo
    contador+=1



