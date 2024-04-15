preco_lata=50.00
litros_lata=5
area_litro=3
altura=float(input("Digite a altura do tanque cilíndrico em metros: "))
raio=float(input("Digite o raio do tanque cilíndrico em metros: "))
area=2*3.14*raio*(raio+altura)
litros=area/area_litro
lata1=(litros/litros_lata)
lata2=int(lata1)
if  lata1 != lata2:
    lata2=lata2+1
    print("batata")
preco_total=lata2*preco_lata
print("Você precisará de",lata2,"latas de tinta e o preço total será de R$",preco_total)