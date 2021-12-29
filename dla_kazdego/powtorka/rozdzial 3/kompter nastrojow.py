# Demonstruje klauzulę elif
import random

print("Jesteś dzisiaj: ")
nastroj = random.randint(1, 4)
if nastroj == 1:
    print("szczęśliwy")
elif nastroj == 2:
    print("obojętny")
elif nastroj == 3:
    print("zły")
else:
    print("Jesteś w naprawdę złym nastroju")
input("\nAby zakończyć naciśnij enter")
