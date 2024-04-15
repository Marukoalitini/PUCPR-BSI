salario=float(input("Digite o seu Sálario: "))
if salario < 1257.13:
    print("O seu sálario é de R$ ",salario," e você está na faixa de isenção do INSS")
if salario >= 1257.13 and salario <= 2512.08:
    taxa1=salario*0.15
    print("O seu sálario é de R$ ", salario, " e você terá que pagar 15% de INSS, o que dá R$ ",taxa1)
if salario > 2512.08:
    taxa2=salario*0.275
    print("O seu sálario é de R$ ", salario, " e você terá que pagar 27.5% de INSS, o que dá R$ ",taxa2)   
