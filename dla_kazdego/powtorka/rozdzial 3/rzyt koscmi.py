# Demonstruje rzut kośćmi
import random

# GEneruj liczby od 1 do 6 na dwóch kostkach
kostka1 = random.randint(1, 6)
kostka2 = random.randrange(6) + 1
razem = kostka1 + kostka2
print("\nWyrzuciłeś raze na dwóch kostkach ", razem, " oczek.")
input("\nAby zakończyć naciśnij enter")
