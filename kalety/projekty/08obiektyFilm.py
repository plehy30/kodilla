class Film:
    def __init__(self, nazwa, rok, odtworzenia=0):
        self.nazwa = nazwa
        self.rok = rok
        self.odtworzenia = odtworzenia

    def __str__(self):
        return "{} ({})".format(self.nazwa, self.rok)


class Serial(Film):
    def __init__(self, nazwa, rok, odtworzenia, sezon, odcinek):
        super().__init__(nazwa, rok, odtworzenia)
        self.sezon = sezon
        self.odcinek = odcinek

    def __str__(self):
        return "{} S{:02d}E{:02d}".format(self.nazwa, self.sezon, self.odcinek)


lista = [Film("Potop", 1975, 10),
         Film("Miś", 1982),
         Serial("Dom", 1975, 0, 2, 4),
         Serial("Droga", 1978, 0, 3, 4),
         Film("Zemsta", 1999, 10)
         ]


def pisz(ll,opis=""):
    print("\n{}".format(opis))
    for x in ll:
        print(str(x))


pisz(lista,"Wszystkie:")

listas = [x for x in lista if isinstance(x,Serial)]
pisz(listas,"Seriale:")

listaf = [x for x in lista if not isinstance(x,Serial)]
pisz(listaf,"Filmy:")
