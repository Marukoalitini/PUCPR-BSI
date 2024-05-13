class TabelaVerdade:
    def __init__(self):
        self.matriz = []

    def atribuicaoValoresTabela(self):
        self.matriz = [['V', 'V']]
        self.matriz.append(['V', 'F'])
        self.matriz.append(['F', 'V'])
        self.matriz.append(['F', 'F'])

    def implicacao_p_q(self):
        for linha in self.matriz:
            a = linha[0]
            b = linha[1]
            if a == 'V' and b == 'F':
                linha.append('F')
            else:
                linha.append('V')

    def conjuncao_p_q(self):
        for linha in self.matriz:
            a = linha[0]
            b = linha[1]
            if a == 'V' and b == 'V':
                linha.append('V')
            else:
                linha.append('F')

    def disjuncao_p_q(self):
        for linha in self.matriz:
            a = linha[0]
            b = linha[1]
            if a == 'V' or b == 'V':
                linha.append('V')
            else:
                linha.append('F')

    def bicondicional_p_q(self):
        for linha in self.matriz:
            a = linha[0]
            b = linha[1]
            if (a == 'V' and b == 'V') or (a == 'F' and b == 'F'):
                linha.append('V')
            else:
                linha.append('F')

class Principal:
    def __init__(self):
        self.tabela = TabelaVerdade()

    def run(self):
        self.tabela.atribuicaoValoresTabela()
        expressaoDigitada = input("Digite uma fórmula com 1 conectivo: ")
        a, operacao, b = expressaoDigitada.split()

        if operacao == '->':
            self.tabela.implicacao_p_q()
        elif operacao == '^':
            self.tabela.conjuncao_p_q()
        elif operacao == 'v':
            self.tabela.disjuncao_p_q()
        elif operacao == '<->':
            self.tabela.bicondicional_p_q()
        for linha in self.tabela.matriz:
            print(f'{linha[0]} {operacao} {linha[1]} = {linha[2]}')

principal = Principal()
principal.run()