# komputer wybiera losowo słowo, a potem miesza w nim litery
# gracz powinien odgadnąć pierwotne słowo
import random

# utwórz sekwencję słów do wyboru
slowa = ("python", "anagram", "łatwy", "skomplikowany", "odpowiedź", "ksylofon")
# wybierz losowo jeden z wyrazów
slowo = random.choice(slowa)
# utwórz zmienną aby później urzyć jej do sprawdzenia czy odpowiedź jest poprawna
correct = slowo
# utwórz pomieszaną wersję słowa
jumble = ""
while slowo:
    pozycja = random.randrange(len(slowo))
    jumble += slowo[pozycja]
    slowo = slowo[:pozycja] + slowo[(pozycja + 1):]

# rozpocznij grę
print(
    """
               Witaj w grze 'Wymieszane litery'!
    
       Uporządkuj litery, aby odtworzyć prawidłowe słowo.
    (Aby zakończyć zgadywanie, naciśnij klawisz Enter bez podawania odpowiedzi.)
    """
)
print("Zgadnij, jakie to słowo:", jumble)
odpowiedz = input("\nTwoja odpowiedź to: ")
while odpowiedz != correct and odpowiedz != "":
    print("\nZłe słowo")
    odpowiedz = input("\nTwoja odpowiedź to: ")
if odpowiedz == correct:
    print("\nZgadłeś")
print("\nDziękuję za grę")
input("\n Aby zakończyć naciśnij enter")
