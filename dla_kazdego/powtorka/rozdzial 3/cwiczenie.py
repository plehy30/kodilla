import random

orzel = 0
reszka = 0

for i in range(100):
    x = random.randint(0, 1)
    if x == 0:
        orzel += 1
    else:
        reszka += 1

print(f"Wylosowano {orzel} orłów i {reszka} reszek")
