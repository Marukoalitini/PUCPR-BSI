ano_nasc=int(input("Digite o ano de nascimento: "))
mes_nasc=int(input("Digite o mês de nascimento: "))
ano_atual=int(input("Digite o ano atual: "))
mes_atual=int(input("Digite o mês atual: "))
idademeses=(ano_atual-ano_nasc)*12+(mes_atual-mes_nasc)
print("Sua idade em meses é:", idademeses)