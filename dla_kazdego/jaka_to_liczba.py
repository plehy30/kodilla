import random

print("\nWitaj w grze 'Jaka to liczba'")
print("\nMam na myśli pewną liczbę z zakresu 1 do 100.")
print("\n Spróbuj ją odgadnąć w jak najniższej liczbie prób")
liczba = random.randint(1, 100)
strzal = int(input("TA liczba to: "))
proba = 1
# pętla zgadywania
while strzal != liczba:
    if strzal > liczba:
        print("Za dużo")
    else:
        print("Za mało")
    strzal = int(input("TA liczba to: "))
    proba += 1
print("Odgadłeś. Ta liczba to ", liczba)
print("Potrzebowałeś ", proba, "prób")
