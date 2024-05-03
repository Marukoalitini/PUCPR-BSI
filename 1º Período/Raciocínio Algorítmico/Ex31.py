notas=[]
for cont_notas in range(5):
    nota=float(input("Digite uma nota: "))
    notas.append(nota)
soma=0
print(notas)
for cont_soma in range(5):
    soma += notas[cont_soma]
print("A soma das notas é: ", soma)
media=soma/len(notas)
print("A média das notas é:", media)