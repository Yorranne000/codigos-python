frase = ("programacao com python é fantástica")
letra = "a"
contagem = 0

for letra in frase:
    if letra == "a" or letra == "á":
     contagem = contagem+1
print(f"A quantidade de letras a é: {contagem}")
