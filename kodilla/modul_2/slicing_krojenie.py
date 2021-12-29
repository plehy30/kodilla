weekdays = ["pon", "wto", "śro", "czw", "pią", "sob", "nie"]
print(weekdays[:3])
print(weekdays[-2])
liczby = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
szesciany = [liczba ** 3 for liczba in liczby]
for liczba in szesciany:
    if liczba % 2 > 0:
        print(liczba, end=", ")
print("\n", szesciany)

lista = [2, 0, 0, 0, 1, 0, 0, 0, 0, 0, 2, 3, 0, 0]
lista_zera1 = []
lista_zera2 = []
lista_zera3 = []
lista_zera1.extend(lista[1:3])
lista_zera1.extend(lista[5:10])
lista_zera1.extend(lista[-2:])
print(lista_zera1)

bez_zer1 = []
bez_zer1.extend(lista[0:1])
bez_zer1.extend(lista[4:5])
bez_zer1.extend(lista[10:12])
print(bez_zer1)
