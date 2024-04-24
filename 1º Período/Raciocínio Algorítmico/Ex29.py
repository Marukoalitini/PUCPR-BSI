pratos = int(input("Digite a quantidade de pratos que serão inseridos o peso: "))
somaprato = 0
pratos800 = 0

for contador in range(pratos):
    pesoprato = float(input("Digite o peso do prato em gramas: "))
    somaprato += pesoprato
    if pesoprato > 800:
        pratos800 += 1

mediaprato = somaprato / 1000 / pratos

print("A média de peso dos pratos é:", mediaprato, "kg.")
print("A quantidade de pratos com peso acima de 800 gramas é:", pratos800)
