vetor=[]
for cont in range(10):
    numero=int(input("Digite um número: "))
    vetor.append(numero)
print("O vetor é:", vetor)
numero=int(input("Digite um número para verificar se está no vetor: "))
if vetor.count(numero)==0:
    print("O número não está no vetor.")
else:
    print("O número está na posição:", vetor.index(numero))