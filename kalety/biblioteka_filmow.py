import random


class Film:
    def __init__(self, tytul, rok, gatunek, odtworzenia=0):
        self.tytul = tytul
        self.rok = rok
        self.gatunek = gatunek
        self.odtworzenia = odtworzenia

    def play(self):
        self.odtworzenia += 1

    def __str__(self):
        return "%s (%d) %d" % (self.tytul, self.rok, self.odtworzenia)


class Serial(Film):
    def __init__(self, tytul, rok, gatunek, odtworzenia, odcinek, sezon):
        super().__init__(tytul, rok, gatunek, odtworzenia)
        self.odcinek = odcinek
        self.sezon = sezon

    def __str__(self):
        # return "%s S%02dE%02d %d" % (self.tytul, self.sezon, self.odcinek,self.odtworzenia)
        return f"{self.tytul} S{self.sezon:02d}E{self.odcinek:02d} {self.odtworzenia}"


lista_filmow = []
lista_filmow.append(Film("Potop", 1970, "historyczny"))
lista_filmow.append(Serial("Dom", 1980, "obyczajowy", 0, 1, 2))
lista_filmow.append(Film("Miś", 1980, "komedia"))
lista_filmow.append(Serial("Daleko", 1980, "obyczajowy", 0, 3, 5))
for f in lista_filmow:
    print(f)

for f in lista_filmow:
    if not isinstance(f, Serial):
        print("%s jest filmem" % (f.tytul))
    else:
        print("%s jest serialem" % (f.tytul))


def search():
    twoj_tytul = input("Podaj tytuł filmu lub serialu: ")
    for f in lista_filmow:
        if twoj_tytul.lower() == f.tytul.lower():
            print(f'Twój film {twoj_tytul} jest na liście')
        else:
            continue


# search()


def generate_views():
    x = random.choice(lista_filmow)
    x.odtworzenia += random.randint(1, 100)


for f in lista_filmow:
    print(f)
print("-----------------------------------")
generate_views()
for f in lista_filmow:
    print(f)


def generate(n):
    for i in range(n):
        generate_views()
        for f in lista_filmow:
            print(f)
        print("-----------------------------------")


generate(10)

lista_filmow.sort(key=lambda film: film.odtworzenia,reverse=True)
for i in range(2):
    print(lista_filmow[i])
print("-----------------------------------")

# import random
#
#
# x = [5, 7, 6, 3, 8, 9]x
#
# print(random.choice(x))
#
#
# print(random.randint(1, 10))
