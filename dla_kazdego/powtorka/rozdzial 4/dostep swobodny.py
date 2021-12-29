# Demonstruje indeksowanie łańcucha znaków
import random

slowo = "indeks"
poczatek = len(slowo)
koniec = -len(slowo)
for i in range(10):
    pozycja = random.randrange(koniec, poczatek)
    print("slowo[", pozycja, "]\t", slowo[pozycja])
input("\nJeżeli chcesz zakończyc naciśnij enter")
