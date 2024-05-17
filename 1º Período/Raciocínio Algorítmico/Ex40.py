nomes = []

for cont in range(3):
    print("Insira o nome do aluno", cont+1, ": ", end="")
    nomes.append(str(input()))
Linhas = 3
Colunas = 3
Notas = [0]*Linhas
for linha in range(Linhas):
    Notas[linha] = [0]*Colunas
for linha in range(Linhas):
    for coluna in range(Colunas):
        print("Insira a nota da prova", coluna+1, "do aluno", nomes[linha], ": ", end="")
        Notas[linha][coluna]=int(input())
for linha in range(Linhas):
    soma = 0
    for coluna in range(Colunas):
        soma += Notas[linha][coluna]
    media=soma/3
    print("A média do Aluno", nomes[linha], 'é',  media)