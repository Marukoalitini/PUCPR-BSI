def validar_intervalo(numero_maior, numero_menor, numero):
    if numero >= numero_menor and numero_maior >= numero:
        return True
    else:
        return False
    
numero=int(input("Digite um número: "))
numeroMaior=int(input("Digite o número maior: "))
numeroMenor=int(input("Digite o número menor: "))

if validar_intervalo(numeroMaior, numeroMenor, numero):
    print("O número está dentro do intervalo")
else:
    print("O número está fora do intervalo")
