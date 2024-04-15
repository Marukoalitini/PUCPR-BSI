contador=0
tabuada=0
numero=int(input("Insira o número para cálculo da tabuada: "))

while contador<11:
    tabuada=numero*contador
    print(numero, "X" , contador, "=", tabuada)
    contador += 1