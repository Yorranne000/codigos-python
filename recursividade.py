#números naturais (soma)

def soma_nat(n):
    for i in range(n):
        soma+=n
        return n +soma_nat(n-1)
    
print(soma_nat())