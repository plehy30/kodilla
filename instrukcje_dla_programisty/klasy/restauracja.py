class Restaurant():

    def __init__(self, name, cuisine_type):
        self.name = name.title()
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Restauracja {self.name} serwuje dania {self.cuisine_type}")

    def open_restaurant(self):
        print(f"Restaurant {self.name} is open")


restauracja1 = Restaurant("Alta", "kuchni włoskiej")
print(restauracja1.name)
print(restauracja1.cuisine_type)
restauracja1.describe_restaurant()
restauracja1.open_restaurant()
