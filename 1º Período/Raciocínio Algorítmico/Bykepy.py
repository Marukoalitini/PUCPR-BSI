#função para comprar creditos
def comprar(qnt, add):
    return qnt + add   

#função para pagar sua utilização
def pagar(qnt, pagar):
    return qnt - pagar

#função para pagar uma utilização de apenas horas no mesmo dia
def pagar_mesmosdia(saida,entrada):
    pagamento=saida-entrada
    return pagamento

#função para pagar uma utilização de horas maiores que 24 horas
def contar_horasMaiores24(saida_dia,entrada_dia,saida_hora,entrada_hora):
    quantidade_dia=saida_dia - entrada_dia
    horas_dia=quantidade_dia * 24
    pagamento=saida_hora - entrada_hora
    return pagamento + horas_dia

#função para pagar uma utilização de algumas horas porem em dias diferentes
def contar_horasMenores24(entrada_hora,saida_hora):
    pagamento=24-entrada_hora
    return pagamento + saida_hora

#listas do historico de dias e horas de utilização
dia_retirada=[]
hora_retirada=[]
minuto_retirada=[]
dia_devoluçao=[]
hora_devoluçao=[]

creditos=0

login="usuario"
senha="12345"


while True:
    #login
    print ("Você precisa logar para utilizar o programa")
    logar = str(input("Login: "))
    colocar_senha = str(input("Senha: "))

    #caso o login estja incorreto
    if login != logar or senha != colocar_senha:
        print("\nLOGIN INCORRETO!\n")

    #caso o login esteja correto
    elif login == logar and colocar_senha == senha:
        print("Login efetuado com sucesso")
        while True:

            #menu de opções
            print("\n\nO que deseja fazer: ")
            escolha1=int(input("[1]Utilizar\n[2]Colocar créditos\n[3]Mostrar Créditos\n[4]Ver meu historico\n[5]Sair\n"))
            
            #comprar creditos
            if escolha1 == 2:
                add=int(input("\n\nQuantos creditos deseja adicionar: R$"))
                if add > 0:
                    creditos= comprar(creditos,add)
                    print("Quantidade de creditos: R$",creditos)
                else:
                    print("\nRecarga inválida")

            #caso o usuario tente utilizar o programa com menos de 5 creditos
            elif escolha1 == 1 and creditos < 5:
                print("\nQuantida de créditos insuficiente, você precisa ter ao menos 5 créditos")

            #Utilizar o programa
            elif escolha1 == 1 and creditos >=5:
                #O dia da retirada e adicionar ao historico
                entrada_dia=int(input("\nQual o dia da retirada da bicicleta: dia "))
                dia_retirada.append(entrada_dia)
                
                #A hora da retirada e adicionar ao historico
                print("\nUse a hora como: 01, 02, 03, ... 23, 24")
                entrada_hora=int(input("Qual a hora da retirada da bicicleta: "))
                hora_retirada.append(entrada_hora)
                
                #O dia da devolução e adicionar ao historico
                saida_dia=int(input("\nQual o dia da devolução da bicicleta: dia "))
                dia_devoluçao.append(saida_dia)
                
                #A hora da devolução e adicionar ao historico
                print("\nUse a hora como: 01, 02, 03, ... 23, 24")
                saida_hora=int(input("Qual a hora da devolução da bicicleta: "))
                hora_devoluçao.append(saida_hora)
                
                #Uilização feita no mesmo dia
                if entrada_dia == saida_dia and entrada_hora < saida_hora:
                    pagamento=pagar_mesmosdia(saida_hora,entrada_hora)
                    creditos=pagar(creditos,pagamento)
                    
                    print("\nUtilização completa, tenha um bom passeio!")
                    print("Total a pagar",pagamento)
                    print("Creditos:",creditos)
                
                #Utilização feita em mais de 24 horas
                elif entrada_dia < saida_dia and entrada_hora <= saida_hora:
                    pagamento=contar_horasMaiores24(saida_dia,entrada_dia,saida_hora,entrada_hora)
                    creditos=pagar(creditos,pagamento)
                    
                    print("Utilização completa, tenha um bom passeio!")
                    print("Total a pagar",pagamento)
                    print("Creditos:",creditos)
                
                #Utilização feita em 2 dias porem menos de 24 horas
                elif entrada_dia < saida_dia and entrada_hora > saida_hora:
                    pagamento=contar_horasMenores24(entrada_hora, saida_hora)
                    creditos=pagar(creditos,pagamento)
                    
                    print("Utilização completa, tenha um bom passeio!")
                    print("Total a pagar",pagamento)
                    print("Creditos:",creditos)
                
                #Caso a contagem de horas seja impossivel de ser feita
                else:
                    print("\nCONTAGEM DE HORAS IMPOSSIVEL!")

            #Mostrar a quantidade de créditos disponivel
            elif escolha1 == 3:
                print("\nSeus créditos são:",creditos,"creditos")

            #Mostrar o historico de utilização
            elif escolha1 == 4:
                print("\n\nDia retirada  ",dia_retirada)
                print("Hora retirada ",hora_retirada)
                print("Dia devolução ",dia_devoluçao)
                print("Hora devolução",hora_devoluçao)
            
            #Sair do programa
            elif escolha1 ==5:
                break
        break


    


        

                



