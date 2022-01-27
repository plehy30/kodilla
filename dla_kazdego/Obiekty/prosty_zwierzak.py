class Critter(object):
    """Wirtualny pupil"""

    def __init__(self, name):
        print("Urodził sie nowy zwierzak")
        self.name = name

    def __str__(self):
        rep = f"Obiekt clasy Critter\n name: {self.name} \n"
        return rep

    def talk(self):
        print("Cześć jestem egzemplarzem klasy Critter")


# Cześć główna
crit1 = Critter("Reksio")
crit2 = Critter("Pucek")
crit1.talk()
crit2.talk()

print("Wyswietlanie obiektu crit1:")
print(crit1)

print("Bezpośrednie wyświetlanie wartości atrybutu crit1.name: ")
print(crit1.name)


input("\nAbe zakończyć naciśnij enter")
