aulas_ras_semanal=int(input("Insira a quantidade de aulas de Ra semanais: "))
semanas=int(input("Insira a quantidade de semanas no semestre: "))
aulas_ra=aulas_ras_semanal*semanas
faltas=aulas_ra*0.25
print("O número de faltas permitidas é:",faltas)