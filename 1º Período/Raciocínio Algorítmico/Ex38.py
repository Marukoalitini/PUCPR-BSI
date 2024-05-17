bigramas=[]
unicos=[]
palavra=str(input("Digite uma palavra: "))
for cont in range(1,len(palavra),1) :
    bigramas.append(palavra[cont-1]+palavra[cont])
for cont in range(0,len(bigramas),1) :
    if bigramas.count(bigramas[cont]) == 1:
        unicos.append(bigramas[cont])
print(palavra, "=", bigramas, ",", len(bigramas), "bigramas e", len(unicos), "únicos:", unicos)
