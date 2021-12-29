# Podsumowanie tego, co już wiemy na temat deklaracji poszczególnych kolekcji. Każdą z nich możemy stworzyć na dwa sposoby.
print("KOLEKCJA: LISTA")
print("""
my_list = [1,2,3]
my_list = list([1,2,3])
""")
print("KOLEKCJA: KROTKA")
print("""
my_tuple = ("mon","tue","wed")
my_tuple = tuple(["mon","tue","wed"])
""")
print("KOLEKCJA: ZBIÓR")
print("""
my_set = {1, 2, 3}
my_set = set([1, 2, 3])
""")
print("KOLEKCJA: SŁOWNIK")
print("""
my_dictionary = {"key1": "value1", "key2": "value2"}
my_dictionary = dict((("key1", "value1"), ("key2", "value2")))
""")
zakupy = {"miesny": ["szynka", "kiełbasa"],
          "piekarnia": ["chleb", "bułki"]}
print("Zakupy w mięsnym: ", zakupy["miesny"])
