# Função para comprar créditos
def comprar_creditos(creditos):
    print("Créditos atuais:", creditos)
    # Se os créditos são negativos, informa o mínimo de créditos que deve ser comprado para zerar a dívida
    if creditos < 0:
        print("Sua conta está negativa. O mínimo de créditos que você pode comprar é", -creditos)
    print("Créditos custam R$1,00 cada.")
    quantidade = int(input("Digite a quantidade de créditos que deseja comprar: "))
    # Verifica se a quantidade comprada é suficiente para zerar a dívida
    while creditos < 0 and quantidade < -creditos:
        print("Quantidade inválida. O mínimo de créditos que você pode comprar é", -creditos)
        quantidade = int(input("Digite a quantidade de créditos que deseja comprar: "))
    # Verifica se a quantidade é positiva
    while quantidade < 0:
        print("Quantidade inválida. Digite uma quantidade maior que 0.")
        quantidade = int(input("Digite a quantidade de créditos que deseja comprar: "))
    # Atualiza os créditos do usuário
    creditos += quantidade
    print("Créditos comprados. Créditos atuais:", creditos)
    return creditos

# Função para calcular a duração da locação em horas
def calcular_duracao_horas(diaretirada, horaretirada, diadevolucao, horadevolucao):
    # Caso a retirada e a devolução ocorram no mesmo dia e a hora de devolução seja posterior à hora de retirada
    if diaretirada == diadevolucao && horaretirada < horadevolucao:
        duracao_horas = horadevolucao - horaretirada
    # Caso a devolução ocorra em um dia posterior à retirada
    elif diaretirada < diadevolucao:
        duracao_horas = (diadevolucao - diaretirada) * 24 + (horadevolucao - horaretirada)
    # Caso a retirada e a devolução ocorram no mesmo dia, mas a hora de retirada seja posterior à hora de devolução
    elif diaretirada == diadevolucao && horaretirada > horadevolucao:
        duracao_horas = 30*24 - (horaretirada - horadevolucao)
    # Caso a devolução ocorra no mês seguinte à retirada
    else:
        duracao_horas = (30 - diaretirada + diadevolucao) * 24 + (horadevolucao - horaretirada)
    return duracao_horas

# Função para registrar uma locação
def registrar_locacao(creditos, locacoes):
    # Verifica se o usuário possui créditos suficientes para uma locação
    if creditos < 5:
        print("Créditos insuficientes para locação.")
        return creditos, locacoes
    # Solicita a data e hora de retirada da locação
    diaretirada = int(input("Digite o dia de retirada: "))
    while diaretirada < 1 or diaretirada > 30:
        print("Dia inválido. Digite um dia entre 1 e 30.")
        diaretirada = int(input("Digite o dia de retirada: "))
    horaretirada = int(input("Digite a hora de retirada: "))
    while horaretirada < 0 or horaretirada > 23:
        print("Hora inválida. Digite uma hora entre 0 e 23.")
        horaretirada = int(input("Digite a hora de retirada: "))
    # Solicita a data e hora de devolução da locação
    diadevolucao = int(input("Digite o dia de devolução: "))
    while diadevolucao < 1 or diadevolucao > 30:
        print("Dia inválido. Digite um dia entre 1 e 30.")
        diadevolucao = int(input("Digite o dia de devolução: "))
    horadevolucao = int(input("Digite a hora de devolução: "))
    while horadevolucao < 0 or horadevolucao > 23:
        print("Hora inválida. Digite uma hora entre 0 e 23.")
        horadevolucao = int(input("Digite a hora de devolução: "))
    # Verifica se a retirada e a devolução ocorrem no mesmo instante
    if diaretirada == diadevolucao and horaretirada == horadevolucao:
        print("Retirada e devolução no mesmo instante. Locação inválida.")
        return creditos, locacoes
    # Calcula a duração da locação
    duracao = calcular_duracao_horas(diaretirada, horaretirada, diadevolucao, horadevolucao)
    # Verifica se a duração da locação é maior que 24 horas
    if duracao > 24:
        print("Sua locação foi de", duracao, "horas, ou", duracao // 24, "dias e", duracao % 24, "horas")
        opcao = str(input("Você tem certeza que inseriu a data corretamente? (S/N): "))
        if opcao == "N":
            return creditos, locacoes
    # Atualiza os créditos do usuário e registra a locação
    creditos -= duracao
    locacoes.append((diaretirada, horaretirada, diadevolucao, horadevolucao))
    
    print("Locação registrada. Créditos atuais:", creditos)
    print("Sua locação foi de", duracao, "horas")
    return creditos, locacoes

# Função para imprimir o relatório de locações
def imprimir_relatorio(creditos, locacoes):
    print('Relatório de utilizações:')
    # Verifica se há locações registradas
    if len(locacoes) == 0:
        print('Nenhuma locação registrada.')
        return
    # Itera sobre as locações registradas e imprime os detalhes
    for cont in range(0, len(locacoes)):
        print("Locação", cont+1, ":")
        print("Dia de retirada:", locacoes[cont][0])
        print("Hora de retirada:", locacoes[cont][1])
        print("Dia de devolução:", locacoes[cont][2])
        print("Hora de devolução:", locacoes[cont][3])

# Função para autenticar o usuário
def autenticar_usuario(Login, Senha):
    user_login = str(input("Insira seu Login: "))
    user_senha = str(input("Insira sua Senha: "))
    # Verifica se o login e a senha inseridos são corretos
    if user_login == Login and user_senha == Senha:
        return True
    else:
        return False

# Função que exibe o menu principal
def menu(creditos, locacoes):
    while True:
        print("\n\nO que deseja fazer: ")
        escolha = int(input("[1]Utilizar\n[2]Colocar créditos\n[3]Mostrar Créditos\n[4]Ver meu histórico\n[5]Deslogar\n[6]Sair\n"))
        # Opção para registrar uma locação
        if escolha == 1:
            creditos, locacoes = registrar_locacao(creditos, locacoes)
        # Opção para comprar créditos
        elif escolha == 2:
            creditos = comprar_creditos(creditos)
        # Opção para mostrar o saldo de créditos atual
        elif escolha == 3:
            print("Créditos atuais:", creditos)
        # Opção para imprimir o relatório de locações
        elif escolha == 4:
            imprimir_relatorio(creditos, locacoes)
        # Opção para deslogar
        elif escolha == 5:
            print("Deslogando...")
            return creditos, locacoes, 0
        # Opção para sair do sistema
        elif escolha == 6:
            print("Saindo...")
            return creditos, locacoes, 1            
        # Caso o usuário insira uma opção inválida
        else:
            print("Opção inválida.")

# Dados do usuário
login = "usuario1"
senha = "senha1"
creditos = 0
locacoes = []

# Loop principal para autenticação e exibição do menu
while True:
    autenticacao = autenticar_usuario(login, senha)
    if autenticacao == True:
        print("Login efetuado com sucesso")
        creditos, locacoes, sair = menu(creditos, locacoes)
    else:
        print("Login ou senha incorretos.")
    if sair == 1:
        break
