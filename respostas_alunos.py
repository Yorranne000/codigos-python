respostas_aluno = ['A', 'C', 'B', 'D', 'A']
gabarito = ['A', 'D', 'B', 'D', 'C']
resultado = 0

for i in range(len(gabarito)):
    if respostas_aluno[i] == gabarito [i]:
        resultado = resultado+1

print(resultado)

