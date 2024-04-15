massa=float(input("Digite a massa inicial em gramas: "))
tempo=0
while massa >= 0.5:
    massa=massa/2
    tempo=tempo+50
print("A massa final é", massa, "gramas, e o tempo decorrido é", tempo, "segundos")
