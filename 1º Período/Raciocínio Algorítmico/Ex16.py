lado1=float(input("Digite o valor do primeiro lado do triângulo: "))
if lado1<=0:
    print("Valor inválido")
    lado1=float(input("Digite, corretamente, o valor do primeiro lado do triângulo: "))  
    if lado1<=0:
        print("Você foi avisado")
        exit()
lado2=float(input("Digite o valor do segundo lado do triângulo: "))
if lado2<=0:
    print("Valor inválido")
    lado2=float(input("Digite, corretamente, o valor do segundo lado do triângulo: "))
    if lado2<=0:
        print("Você foi avisado")
        exit()
lado3=float(input("Digite o valor do terceiro lado do triângulo: "))
if lado3<=0:
    print("Valor inválido")
    lado3=float(input("Digite, corretamente o valor do terceiro lado do triângulo: "))
    if lado3<=0:
        print("Você foi avisado")
        exit()
if lado1+lado2>lado3 and lado1+lado3>lado2 and lado2+lado3>lado1:
    if lado1==lado2 and lado2==lado3:
        print("Esse é um Triângulo Equilátero")
    elif  lado1==lado2 and lado2!=lado3 or lado2==lado3 and lado3!=lado1 or lado3==lado1 and lado1!=lado2:
        print("Esse triângulo é isóceles")
    else:
        print("Esse é um triângulo escaleno")
else:
    print("Isso não é um triângulo")