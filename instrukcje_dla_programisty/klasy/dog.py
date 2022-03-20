class Dog():
    """Prosta póba modelowania psa"""

    def __init__(self, name, age):
        """Inicjalizacja atrybutów name i age"""
        self.name = name
        self.age = age

    def sit(self):
        """Symulacja, że pies siedzi"""
        print(f"{self.name.title()} teraz siedzi")

    def roll_over(self):
        """Symulacja, że pies teraz leży"""
        print(f"{self.name.title()} teraz położył się")


my_dog = Dog("willie", 4)
my_dog.sit()
my_dog.roll_over()
print(my_dog.name.title())
print(f"Mój pies ma {my_dog.age} lata")
