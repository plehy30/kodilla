liczby = [1, 3, 5, 11, 20]
ich_kwadraty = []
for number in liczby:
    ich_kwadraty.append(number * number)
print("Liczby: ", liczby)
print("Ich kwadraty: ", ich_kwadraty)
kwadrat_prosciej = [number * number for number in liczby if number > 10]
print(f"Te kwadraty {kwadrat_prosciej} z listy {liczby}.")
