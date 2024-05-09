sorteio = []
for cont in range(6):
    sorteio.append(int(input("Digite um  do resultado do sorteio: ")))
aposta = []
for cont in range(6):
    aposta.append(int(input("Digite um número da sua aposta: ")))
acertos = 0
for contSorteio in range(len(sorteio)):
    for contAposta in range(len(aposta)):
        if sorteio[contSorteio] == aposta[contAposta]:
            acertos += 1
print("Você acertou", acertos, "números.")