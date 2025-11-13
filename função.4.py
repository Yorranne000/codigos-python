#Imposto e descontos utilizando função (def)


def taxa(valor):
    if valor<=50:
        imposto=valor*0.20
        icms=(valor+imposto)*0.20
        return valor+imposto+icms
    else:
        imposto = (valor*0.60) -20
        icms = (valor+imposto) * 0.20
        return valor+imposto+icms
print(taxa(valor=float(input("Digite o valor do produto: "))))

