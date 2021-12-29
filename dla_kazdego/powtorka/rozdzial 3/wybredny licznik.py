# Demonstruje instrukcje break i continue
licznik = 0
while True:
    licznik += 1
    if licznik > 10:
        break
    if licznik == 4:
        continue
    print(licznik)
