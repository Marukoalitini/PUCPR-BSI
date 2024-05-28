pistas=[
    
]
deducoes=[

]
pistasescolhidas=[]
print("Bem-vindo ao jogo Enigma do castelo.")
print("A História se passa em uma antiga cidade medieval, onde um castelo foi construído para proteger um tesouro muito valioso.")
print("O tesouro foi escondido em um local muito secreto do castelo, onde apenas o rei sabia onde estava.")
print("Um dia o rei percebeu que seu precioso tesouro havia sido roubado.")
print("O rei então chamou os melhores detetives do reino para desvendar o mistério do roubo do tesouro.")]
print("Seu objetivo é reunir pistas e deduzir quem foi o responsável por roubar o tesouro e onde ele ocorreu."))
while True:
    if len(pistasescolhidas)==4:
        print("Você já escolheu todas as pistas.")
        print("\nPistas desvendadas: ")
        for pista in pistasescolhidas:
            print(pista)
        break
    elif len(pistasescolhidas)>0:
        print("\nTodas as pistas escolhidas até agora: ")
        for pista in pistasescolhidas:
            print(pista)

    print("\nEscolha uma pista para desvendar a história.")
    escolha=int(input("Digite um número de 1 a 4 para escolher a pista ou 0 para sair."))
    if escolha==0:
        break
    elif escolha in range(1,5) :
        if pistas[escolha-1] in pistasescolhidas:
            print("Pista já escolhida.")
        else:
            pistasescolhidas.append(pistas[escolha-1])
            print("Pista escolhida: ",pistas[escolha-1])
    else:
        print("Opção inválida.")
while True:
    senha=input("Digite a senha para Acessar as deduções:")
    if senha=="1234":
        print("Deduções:")
        for deducao in deducoes:
            print(deducao)
        break
    elif senha=="4321":
        deducoesescolhidas=[]
        while True:
            if len(deducoesescolhidas)==2:
                print("Você já escolheu todas as deduções.")
                print("\nDeduções desvendadas: ")
                for deducao in deducoesescolhidas:
                    print(deducao)
                break
            elif len(deducoesescolhidas)>0:
                print("\nTodas as deduções escolhidas até agora: ")
                for deducao in deducoesescolhidas:
                    print(deducao)

            print("\nEscolha uma dedução para desvendar a história.")
            escolha=int(input("Digite um número de 1 a 2 para escolher a dedução ou 0 para sair."))
            if escolha==0:
                break
            elif escolha in range(1,3) :
                if deducoes[escolha-1] in deducoesescolhidas:
                    print("Dedução já escolhida.")
                else:
                    deducoesescolhidas.append(deducoes[escolha-1])
                    print("Dedução escolhida: ",deducoes[escolha-1])
            else:
                print("Opção inválida.")
    else:
        print("Senha incorreta.")