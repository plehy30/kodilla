# Demonstruje atrybuty klasy i metody statyczne

class Critter(object):
    """Wirtualny pupil"""
    total = 0

    @staticmethod
    def status():
        print("\nOgólna liczba zwierzaków wynosi ", Critter.total)

    def __init__(self, name):
        print("Urodził sie zwierzak")
        self.name = name
        Critter.total += 1


# CZęść główna

print("Uzyskanie dostepu do atrybutu klasy Critter.total: ", end=" ")
print(Critter.total)

print("\nTworzenie zwierzaków.")
crit1 = Critter("Zwierzak 1")
crit2 = Critter("Zwierzak 2")
crit3 = Critter("Zwierzak 3")

Critter.status()

print("\nUzyskanie dostepu do atrybutu klasy poprzez obiekt:")
print(crit1.total)

input("\nAby zakończyć naciśnij enter")
