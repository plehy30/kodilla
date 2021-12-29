# Komputer wybiera losowo słowo, a potem miesza wnim litery
# Gracz odgaduje jakie to słowo

import random

# utwórz krotkę ze słowami do wyboru
SLOWA = ("python", "anagram", "łatwy", "skomplikowany", "odpowiedź", "ksylofon")
# wybierz losowo słowo
slowo = random.choice(SLOWA)
# utwórz zmienną by później porównać ją z wybranym słowem
prawidlowe = slowo
# utwórz pomieszaną wersje słowa
pomieszana = ""
while slowo:
    pozycja = random.randrange(len(slowo))
    pomieszana += slowo[pozycja]
    slowo = slowo[:pozycja] + slowo[(pozycja + 1):]
# rozpocznij grę
print(
    """
               Witaj w grze 'Wymieszane litery'!
    
       Uporządkuj litery, aby odtworzyć prawidłowe słowo.
    (Aby zakończyć zgadywanie, naciśnij klawisz Enter bez podawania odpowiedzi.)
    """
)
print("Zgadnij, jakie to słowo:", pomieszana)
odpowiedz = input("Twoja odpowiedź")
while odpowiedz != prawidlowe and odpowiedz != "":
    print("Niestety to nie to słowo")
    odpowiedz = input("Twoja odpowiedź")
if odpowiedz == prawidlowe:
    print("Zgadłeś\n")
print("Dziękuję za udział w grze.")

input("\n\nAby zakończyć program, naciśnij klawisz Enter.")
