def teste_cpf(cpf):
    if len(cpf) == 11:
        pesos=[10,9,8,7,6,5,4,3,2]
        pesos2=[11,10,9,8,7,6,5,4,3,2]
        somad10=0
        somad11=0
        for i in range(9):
            somad10+=int(cpf[i])*pesos[i]
            somad11+=int(cpf[i])*pesos2[i]
        d10= 11 - (somad10 % 11)
        if d10 > 9:
            d10 = 0
        somad11+=d10*pesos2[9]
        d11= 11 - (somad11 % 11)
        if d11 > 9:
            d11 = 0
        if int(cpf[9]) == d10 and int(cpf[10]) == d11:
            return True
        else:
            return False
    else:
        return False

cpf=str(input("Digite o CPF: "))
if teste_cpf(cpf):
    print("CPF válido")
else:
    print("CPF inválido")
    