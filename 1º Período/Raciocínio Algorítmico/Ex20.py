numero=int(input("Insira um número de 1 a 100:"))
adivinhar=int(input("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nDê o computador para outra pessoa e peça para ela adivinhar o número:"))
while adivinhar != numero:
    if adivinhar > numero:
        print("Você errou, tente um número menor")
    elif adivinhar < numero:
        print("Você errou, tente um número maior")
    adivinhar=int(input("Insira um novo número: "))
print("Você acertou")