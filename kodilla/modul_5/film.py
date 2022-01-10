class Film:
    def __init__(self, tytul):
        self.tytul = tytul
        self.counter = 0

    def play(self):
        self.counter += 1

    def __str__(self):
        return f"{self.tytul}"


class Serial(Film):

    def __init__(self, tytul, epizod):
        super().__init__(tytul)
        self.epizod = epizod

    def __str__(self):
        return f"{self.tytul}, epizod: {self.epizod}"


movies = [
    Film("Władca Pierscieni"),
    Serial("The Expanse", 1),
    Film("Forest Gump")
]


def get_films(movies):
    list_of_films = [film for film in movies if isinstance(film, Film) and not isinstance(film, Serial)]
    return list_of_films
