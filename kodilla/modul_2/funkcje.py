greetings = "cześć poskramiaczu lwów"
print(type(greetings))
print(greetings.upper())
print("metody dla stringów: ", dir(greetings))
lista_zakupow = ["buraki", "masło", "chleb"]
print(len(lista_zakupow))
print("metody dla list: ", dir(lista_zakupow))
# rozpakowywanie krotek:
days = ("pon", "wto", "sro")
dzien_1, dzien_2, dzien_3 = days
print(dzien_2)
print(days[1])
# Funkcje zbiorów:
zakupy_a = {"pieczywo", "masło", "ser"}
zakupy_b = {"wędlina", "masło", "cytryna"}
# suma zbiorów
suma_zakopow = zakupy_b | zakupy_b
suma_zakopow_2 = zakupy_a.union(zakupy_b)
print(suma_zakopow)
print(suma_zakopow_2)
# Iloczyn zbiorów czyli ich częśc wspólna:
iloczyn_zakupow = zakupy_a & zakupy_b
iloczyn_zakupow_2 = zakupy_a.intersection(zakupy_b)
print(iloczyn_zakupow)
print(iloczyn_zakupow_2)
# Róznica zbiorów:
roznica_zakopow = zakupy_a - zakupy_b
roznica_zakopow_2 = zakupy_a.difference(zakupy_b)
print(roznica_zakopow)
print(roznica_zakopow_2)
# Funkcje słownika:
moje_zakupy = {"piekarnia": ["chleb", "bułki"],
               "warzywniak": ["marchew", "pomidory"]}
print(moje_zakupy.keys())
print(moje_zakupy.values())
print(moje_zakupy.get("piekarnia"))

