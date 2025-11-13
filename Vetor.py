#Informar 3 nomes. Mostrar quantas letras "A" e "E"
#possuem. OBS.: O srt é um vetor de caracteres.

nome1= input("Informe o primeiro nome: ")
nome2= input("Informe o segundo nome: ")
nome3=input("Informe o terceiro nome: ")
a=0
e=0     
for letra in nome1:
    if letra == "a":
        a+=1
    elif letra == "e":
        e+=1
print(f" O nome {nome1} possue {a} 'a' e {e} 'e'")

a=0
e= 0
for letra in nome2:
    if letra == "a":
        a+=1
    elif letra == "e":
        e+=1
print(f" O nome {nome2} possue {a} 'a' e {e} 'e'")

a=0
e= 0
for letra in nome3:
    if letra == "a":
        a+=1
    elif letra == "e":
        e+=1
print(f" O nome {nome3} possue {a} 'a' e {e} 'e'")

