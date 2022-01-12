class Zwierze():
    def __init__(self, nazwa, plec, wiek, waga, rodzaj,wzrost):
        self.nazwa = nazwa
        self.plec = plec
        self.wiek = wiek
        self.waga = waga
        self.rodzaj = rodzaj
        self.wzrost=wzrost
    @property
    def stosunek(self):
        return self.waga/self.wzrost


animal1 = Zwierze("koń", False, 5, 300, 'ssak',300)
animal2 = Zwierze("pies", True, 15, 20, 'ssak',50)
animal3 = Zwierze('kot', False, 7, 4, 'ssak',45)
animal4 = Zwierze('karp', False, 1, 2, 'ryba',30)
animal5 = Zwierze('papuga', True, 10, 1, 'ptak',30)
animals = [animal1, animal2, animal3, animal4, animal5]

for a in animals:
    animals.sort(key=lambda a: a.stosunek)
print(f"zwierzę z najwyższym stosunkiem: {animals[0].nazwa}")
animals.sort(key=lambda animal: animal.nazwa)
print(f"posortowane po nazwie: ")
for a in animals:
    print(a.nazwa)
# animals.sort(key=lambda a: a.wiek)
# print(f"posortowane po wieku: {animals.wiek}")
