Linhas=2
Colunas=2
matriz = [0]*Linhas
for linha in range(Linhas):
    matriz[linha] = [0]*Colunas
for linha in range(Linhas):
    for coluna in range(Colunas):
        matriz[linha][coluna]=int(input("Insira um número: "))
for linha in range(Linhas):
    soma = 0
    for coluna in range(Colunas):
        soma += matriz[linha][coluna]
    print("A soma da linha", matriz[linha], "é", soma)