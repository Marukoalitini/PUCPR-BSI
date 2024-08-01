import random


def retornar_lista(tamanho):
    lista = []
    for  cont in range(tamanho):
        lista.append(random.randint(1,1000))
    return lista
quantidade = int(input("Insira a quantidade de números para criar uma lista:"))
Lista = retornar_lista(quantidade)
for cont in range(len(Lista)):
    if Lista[cont] % 3 == 0:
        print("O número", Lista[cont], "é múltiplo de 3")
    if Lista[cont] % 2 == 0:
        print("O número", Lista[cont], "é par")
    if Lista[cont] % 2 != 0:
        print("O número", Lista[cont], "é impar")
    