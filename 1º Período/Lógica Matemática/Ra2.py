pistas=[
    "1- Sir Cedric, o valente cavaleiro responsável pela guarda do castelo, estava no castelo na noite do roubo.",
    "2- Se Lady Evelyn, uma nobre dama conhecida por sua perspicácia e inteligência, estava em seus aposentos, então Sir Cedric não estava no castelo na noite do roubo.",
    "3- Se Lady Evelyn, não estava em seus aposentos, então ela estava bebendo com o ferreiro na taverna.",
    "4- Se Alexandre, o Ferreiro, estava na taverna, então ele não era o responsável pelo roubo.",
    "5- Se Sir Cedric estava no castelo na noite do roubo, então o roubo ocorreu na sala do trono.",
    "6- Se o roubo ocorreu na sala do trono, então o responsável pelo roubo foi o bobo da corte,que frequentava a sala do trono para entreter o Rei, ou o Ferreiro, que conhecia os calabouços do castelo.",
    "7- Frei Benedictus, o monge, tinha inveja do rei."   
]
deducoes=[
    "1- Pista 1 e 2: Lady Evelyn não estava em seus aposentos.",
    "2- Pista 3 e 4: Marcelo, o Ferreiro, não era o responsável pelo roubo.",
    "3- Pista 5 e 1: O roubo ocorreu na sala do trono.",
    "4- Pista 6 e dedução 3: O responsável pelo roubo foi o bobo da corte ou o ferreiro.",
    "5- Dedução 4 e 2: O responsável pelo roubo foi o bobo da corte."
]
pistasescolhidas=[]
print("Bem-vindo ao jogo Enigma do castelo.")
print("A História se passa em uma antiga cidade medieval, onde um castelo foi construído para proteger um tesouro muito valioso.")
print("O tesouro foi escondido em um local muito secreto do castelo, onde apenas o rei sabia onde estava.")
print("Um dia o rei percebeu que seu precioso tesouro havia sido roubado.")
print("O rei então chamou os melhores detetives do reino para desvendar o mistério do roubo do tesouro.")
print("Seu objetivo é reunir pistas e deduzir quem foi o responsável por roubar o tesouro e onde ele ocorreu.")
print("Os suspeitos são Sir Cedric, o cavaleiro responsável pela guarda do castelo, Lady Evelyn, uma dama jovem e astuta, Alexandre, o Ferreiro que conhecia os calabouços do castelo, o bobo da corte, que servia diretamente ao rei e Frei Benedictus, o monge que aconselhava o rei.")
while True:
    if len(pistasescolhidas)==7:
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
    escolha=int(input("Digite um número de 1 a 7 para escolher a pista ou 0 para sair: "))
    if escolha==0:
        break
    elif escolha in range(1,8) :
        if pistas[escolha-1] in pistasescolhidas:
            print("Pista já escolhida.")
        else:
            pistasescolhidas.append(pistas[escolha-1])
            print("Pista escolhida: ",pistas[escolha-1])
    else:
        print("Opção inválida.")
if len(pistasescolhidas)>0:
        print("\nTodas as pistas descobertas durante a investigação: ")
        for pista in pistasescolhidas:
            print(pista)

while True:
    print("\n")
    senha=input("Digite a senha para Acessar as deduções:")
    if senha=="1234":
        print("Deduções:")
        for deducao in deducoes:
            print(deducao)
        input()
        break
    elif senha=="4321":
        deducoesescolhidas=[]
        while True:
            if len(deducoesescolhidas)==5:
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
            escolha=int(input("Digite um número de 1 a 5 para escolher a dedução ou 0 para sair."))
            if escolha==0:
                break
            elif escolha in range(1,6) :
                if deducoes[escolha-1] in deducoesescolhidas:
                    print("Dedução já escolhida.")
                else:
                    deducoesescolhidas.append(deducoes[escolha-1])
                    print("Dedução escolhida: ",deducoes[escolha-1])
            else:
                print("Opção inválida.")
    else:
        print("Senha incorreta.")