numero_entradas=float(input("Digite o número de entradas: "))
valor_entradas=float(input("Digite o valor de cada entrada: "))
desconto=float(input("Digite a porcentagem do desconto: "))
estacionamento=float(input("Digite o valor do estacionamento: "))
total_entradas=numero_entradas*valor_entradas
pagamento=total_entradas-(total_entradas*desconto/100)+estacionamento
print("O valor a ser pago é de R$",pagamento)