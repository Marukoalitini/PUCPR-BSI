vogais = 0
espaco = 0
texto = str(input("Digite um texto: "))
for cont in range(len(texto)):
    if texto[cont] in 'AaÁáÀàÃãÂâEeÉéÈèÊêIiÍíÌìÎîOoÓóÒòÕõÔôUuÚúÙùÛû':
        vogais += 1
    elif texto[cont] == ' ':
        espaco += 1
print("O texto possui", vogais, "vogais e", espaco, "espaços em branco.")