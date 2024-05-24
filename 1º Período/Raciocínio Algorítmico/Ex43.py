def soma(valor1, valor2):
    return valor1 + valor2
def subtracao(valor1, valor2):
    return valor1 - valor2
def multiplicacao(valor1, valor2):
    return valor1 * valor2
def divisao(valor1, valor2):
    return valor1 / valor2

valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))
escolha = int(input("Digite 1 para soma, 2 para subtração, 3 para multiplicação e 4 para divisão: "))
if escolha == 1:
    print("A soma é: ", soma(valor1, valor2))
elif escolha == 2:
    print("A subtração é: ", subtracao(valor1, valor2))
elif escolha == 3:
    print("A multiplicação é: ", multiplicacao(valor1, valor2))
elif escolha == 4:
    print("A divisão é: ", divisao(valor1, valor2))
else:
    print("Opção inválida")
