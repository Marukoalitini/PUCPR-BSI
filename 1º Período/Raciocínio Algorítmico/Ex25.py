numero=int(input("Digite um número positivo ou neutro: "))
while numero<0:
    numero=int(input("Incorreto, escreva um número positivo ou neutro: "))
if numero==0:
    fatorial=1
elif numero>0:
    fatorial=1
    for contador in range(numero,0,-1):
        fatorial=fatorial*contador
print("O fatorial de", numero, "é", fatorial)