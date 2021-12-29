import random

liczba = random.randint(1, 100)
odpowiedz = int(input("Ta liczba to: "))
proba = 1

while odpowiedz != liczba:
    if odpowiedz > liczba:
        print("Za dużo")
    else:
        print("Za mało")
    odpowiedz = int(input("Ta liczba to: "))
    proba += 1
print("odgadłeś, ta liczba to: ", liczba)
print("zrobiłeś to w ", proba, " próbach")
input("\nAby zakończyć naciśnij enter")
