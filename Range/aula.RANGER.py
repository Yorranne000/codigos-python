
#lista de números pares até 10000
for i in range (2,10001,2):
   print(i)

#Tirar um nome repetido
instrumentos_musicais = ["Piano", "Violão", "Bateria", "Teclado", "Piano", "Baixo", "Guitarra", "Saxofone", "Gaita", "Piano"]
instrumentos_musicais.sort()

for i in range(len(instrumentos_musicais)):
        if "Piano" in instrumentos_musicais:
                instrumentos_musicais.remove("Piano")
print(instrumentos_musicais)

