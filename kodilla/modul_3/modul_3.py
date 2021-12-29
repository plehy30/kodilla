# Zadanie 1
moje_zakupy = {"piekarnia": ["chleb", "bułki"],
               "warzywniak": ["marchew", "pomidory"]}
for values in moje_zakupy.values():
    print("Wchdzę do warzywniaka i kupuję: ", moje_zakupy["warzywniak"], "a potem wchodzę do piekarni i kupuję: ",
         moje_zakupy["piekarnia"], "wszystkich produktów jest: ",len(moje_zakupy.values()))

# Zadanie 2
podzielne_5 = []
for i in range(0, 100):
    if i % 5 == 0:
        podzielne_5.append(i)
print(podzielne_5)
# kwadrat_prosciej = [number * number for number in liczby if number > 10]
potegi_3 = [liczba ** 3 for liczba in podzielne_5]
print(potegi_3)
