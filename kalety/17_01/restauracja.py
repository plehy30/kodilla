class Restaurant:
    def __init__(self, restaurant_name, cousine_type):
        self.restaurant_name = restaurant_name
        self.cousine_type = cousine_type
        self.open_hours = '8-22'

    def describe_restaurant(self):
        print(f'Restauracja {self.restaurant_name} serwuje kuchnię {self.cousine_type}')

    def open_restaurant(self):
        print(f'Restauracja {self.restaurant_name} jest otwarta w godzinach {self.open_hours}')


class User:
    def __init__(self, first_name, last_name, stanowisko, age=45):
        self.first_name = first_name
        self.last_name = last_name
        self.stanowisko = stanowisko
        self.age = age

    def describe_user(self):
        print(f'Pracownik {self.first_name} {self.last_name} {self.stanowisko} lat {self.age}')

    def __str__(self):
        return f'Pracownik {self.first_name} {self.last_name} {self.stanowisko} lat {self.age}'

    def greet_user(self):
        print(f'Witaj {self.first_name} {self.last_name}')


p1 = User('Tomasz', 'Lecz', 'szef', 50)
p1.describe_user()
p1.greet_user()
print(p1)
p2 = User('Andrzej', 'Jot', "kucharz")
p2.describe_user()

restauracja1 = Restaurant('Kasia', "pączkarnia")
restauracja1.describe_restaurant()
restauracja1.open_restaurant()
