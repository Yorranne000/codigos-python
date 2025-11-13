nomes = ["Davi", "Maria", "Kelvin"]
a=0
e=0

for i in range (len(nomes)):
    for j in range (len(nomes[i])):
        if nomes[i][j]=="a":
            a+=1
        elif nomes [i][j] == "e":
            e+=1
    print(f"O nome {nomes[i]} possui {a} 'a' e {e} 'e'")
    a=0
    b=0 