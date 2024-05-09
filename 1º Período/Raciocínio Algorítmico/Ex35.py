mercadoria = []
quantidade = []
preco = []
faturamento= []
faturamentototal=0
for cont in range(100):
    mercadoria.append(cont+1)
    print("Mercadoria", cont+1)
    quantidade.append(int(input("Digite a quantidade: ")))
    preco.append(float(input("Digite o preço: ")))
    faturamento.append(quantidade[cont]*preco[cont])
    faturamentototal+=faturamento[cont]
print("Mercadoria\tQuantidade\tPreço\tFaturamento")
for cont in range(100):
    print(mercadoria[cont],"\t\t",quantidade[cont],"\t\t",preco[cont],"\t",faturamento[cont])
print("Faturamento total:", faturamentototal)
