# Modyfikowanie listy:
# Podmiana:
lista_zakupow = ["buraki", "masło", "chleb"]
lista_zakupow[2] = "chleb bezglutenowy"
print(lista_zakupow)
# Dodawanie:
lista_zakupow.append("tuńczyk")
lista_zakupow = lista_zakupow + ["tuńczyk"]
print(lista_zakupow)
kierunki = ["wschód", "zachód"]
kierunki = kierunki + ["północ"]
kierunki.append("południe")
print(kierunki)
# Pomniejszanie - usuwanie:
del lista_zakupow[1]
print(lista_zakupow)
lista_zakupow.remove("chleb bezglutenowy")
print(lista_zakupow)
lista_zakupow.append("masło", )
lista_zakupow.append("chleb")
print(lista_zakupow)
# porządkowanie - sortowanie:
posortowana_lista_zakupow = sorted(lista_zakupow)
print(posortowana_lista_zakupow)
print(f"To jest posortowana lista zakupów {posortowana_lista_zakupow}")
lista_zakupow.sort()
print(f"To jest posortowana lista zakupów {lista_zakupow}")


