def greet_ussers(names):
    """Wyświetla powitanie każdemu uzytkownikowi"""
    for name in names:
        msg = f"Witaj {name.title()}"
        print(msg)


username = ['halina', 'tomek', 'marzena']
greet_ussers(username)
niewydrukowane = ['telefon', 'robot', 'figura']
wydrukowane = []
while niewydrukowane:
    drukowane = niewydrukowane.pop()
    print(f"Trwa drukowanie {drukowane}")
    wydrukowane.append(drukowane)

print("\nWydrukowane zostały nastepujące modele:")
for sztuki in wydrukowane:
    print(sztuki)


def drukowanie(niewydrukowane, wydrukowane):
    while niewydrukowane:
        drukowane = niewydrukowane.pop()
        wydrukowane.append(drukowane)


def pokaz_skonczone(wydrukowane):
    print("\nWydrukowane zostały: ")
    for sztuki in wydrukowane:
        print(sztuki)


niewydrukowane = ['kostka', 'walec', 'szklanka']
wydrukowane = []
drukowanie(niewydrukowane, wydrukowane)
pokaz_skonczone(wydrukowane)
