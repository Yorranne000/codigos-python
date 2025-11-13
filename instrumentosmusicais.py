'''instrumentos_musicais = ["Piano", "Violão", "Bateria", "Teclado", "Piano", "Baixo", "Guitarra", "Saxofone", "Gaita", "Piano"]
instrumentos_musicais.sort()

for instrumentos in instrumentos_musicais:
    if "Piano" in instrumentos_musicais:
        instrumentos_musicais.remove("Piano")
print(instrumentos_musicais)'''
    
 
instrumentos_musicais = ["Piano", "Violão", "Bateria", "Teclado", "Piano", "Baixo", "Guitarra", "Saxofone", "Gaita", "Piano"]
instrumentos_musicais.sort()

for i in range(len(instrumentos_musicais)):
        if "Piano" in instrumentos_musicais:
                instrumentos_musicais.remove("Piano")
print(instrumentos_musicais)
 