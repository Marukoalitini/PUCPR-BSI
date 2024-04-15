maiornumero=int(input("Digite um número: "))
for cont in range(4):
    numero=int(input("Digite um número: "))
    if numero>maiornumero:
        maiornumero=numero
print("O maior número lido é", maiornumero)