L1=float(input( "Informe o lado direito do triângulo: "))
L2=float(input( "Informe o lado esquerdo do triângulo "))
L3=float(input( "Informe a base do triângulo "))
if L1+L2 > L3 and L1 + L3 > L2 and L2 + L3> L1:
    if L1 == L2 == L3:
        print("O triângulo é equilátero!")
    elif L1 == L2 or L1 == L3 or L2 == L3:
        print("O triângulo é isósceles!")
    else:
        print("O triângulo é escaleno!")
else:
        print("A base não forma um triângulo.")

