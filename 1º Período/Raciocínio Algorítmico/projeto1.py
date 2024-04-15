Saldo=0.00
Passagem=5.50
Programa=0
while Programa==0:
    usuario=int(input("Digite o número 1 para entrar no menu de Usuário, ou 2 para o menu de Administrador: "))
    if usuario==2:
        senha=int(input("Digite a senha de Administrador: "))
        if senha==2764:
            menuAdmin=0
            while menuAdmin==0:
                print("## Menu ADMIN ##")
                print("1-Visualizar o Saldo do Cartão")
                print("2-Definir o valor da passagem")
                print("3-Sair do menu de Administrador")
                print("4-Fechar o programa")
                opcaoAdmin=int(input("Digite a opção desejada: "))
                if opcaoAdmin==1:
                    print("O saldo do cartão é de R$ ", Saldo, ".")
                elif opcaoAdmin==2:
                    print("O valor atual da passagem é de R$", Passagem, ".")
                    Passagem=float(input("Insira o novo preço da passagem: "))
                    while Passagem<0:
                        Passagem=float(print("Valor inválido, por favor insira um valor positivo para o novo preço da passagem: "))
                    print("O valor da passagem foi alterado para R$", Passagem, ".")
                elif opcaoAdmin==3:
                    menuAdmin=1
                    print("Saindo do menu de Administrador.")
                elif opcaoAdmin==4:
                    menuAdmin=1
                    Programa=1
                    print("Fechando o programa.")
                else: 
                    print("Opção inválida.")
        else:
            print("Senha incorreta, voltando ao menu de seleção de usuário.")
    elif usuario==1:
        menuUsuario=0
        while menuUsuario==0:
            print("Menu de Usuário")
            print("1-Usar passagem")
            print("2-Consultar Saldo")
            print("3-Carregar Cartão")
            print("4-Sair do menu de usuário")
            opcaoUsuario=int(input("Digite a opção desejada: "))
            if opcaoUsuario==1:
                quantidadePassagens=int(input("Insira quantas passagens você deseja usar: "))
                while quantidadePassagens<=0:
                    quantidadePassagens=int(input("Quantidade inválida, por favor insira um número positivo para a quantidade de passagens: "))
                precoPassagem=quantidadePassagens*Passagem
                if Saldo<precoPassagem:
                    faltaSaldo=precoPassagem-Saldo
                    print("Seu saldo atual é insuficiente para essa compra, faltam R$", faltaSaldo, '.')
                else:
                    Saldo=Saldo-precoPassagem
                    print("Você usou", quantidadePassagens, "passagens, e restam R$", Saldo, "nesse cartão.")
            elif opcaoUsuario==2:
                print("Seu saldo atual é de R$", Saldo, ".")
            elif opcaoUsuario==3:
                carregarSaldo=int(input("Insira o valor que deseja carregar: "))
                while carregarSaldo<=0:
                    carregarSaldo=int(input("Quantidade inválida, por favor insira um número positivo para a carga de saldo: "))
                Saldo=Saldo+carregarSaldo
                print("Foram adicionados R$", carregarSaldo, "ao seu saldo, e o saldo atual é de R$", Saldo, ".")
            elif opcaoUsuario==4:
                menuUsuario=1
                print("Saindo do menu de Usuário.")
            else: 
                print("Opção inválida.")    
    else:
        print("Opção inválida.")