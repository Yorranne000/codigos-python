#Consumo Descrição
Distância=int(input("Informe a distância total pecorrida: "))
Combustivel= float(input("Digite o total de combustível gasto em litros: "))
Consumo= Distância / Combustivel
if Consumo == int(Consumo):
    print(str(Consumo) + "Km/l")
else:
    print(str(round(Consumo, 3)) + "Km/l")
          


