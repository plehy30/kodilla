def favorite_book(title):
    print(f"Moja ulubiona książka ma tytuł {title}.")


favorite_book("Książka")


def describe_pet(animal_name, animal_type="pies"):
    """Wyswietla informcje o zwierzęciu"""
    print(f"\n Moje zwierzę to {animal_type}")
    print(f"Mój {animal_type} ma na imię {animal_name.title()}")


describe_pet("harry")


# describe_pet(animal_name="harry", animal_type="chomik")

def make_shirt(size="XXL", text="Uwielbiam Pythona"):
    print(f"Moja koszulka ma rozmiar {size} i ma napis: {text}")


make_shirt()
make_shirt(size="L")


def get_forrmated_name(first_name, last_name, middle_name=""):
    """Zwraca elegancko sformatowane pełne imie i nazwisko"""
    if middle_name:
        full_name = f"{first_name} {last_name} {middle_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()


musician = get_forrmated_name("jimi", "hendrix")
print(musician)
musician = get_forrmated_name("john", "lee", 'hooker')
print(musician)


def build_person(first_name, last_name, age=None):
    """Zwraca słownik informacji"""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person


musician = build_person('jimi', 'hendrix', age=27)
print(musician)


def make_album(name, title_alboom, liczba=None):
    plyta = {'nazwa': name, 'tytul': title_alboom}
    if liczba:
        plyta['liczba'] = liczba
    return plyta


while True:
    print('Podaj artystę: ')
    print('Jeśli chcesz zakończyć napisz q')
    artysta = input('Artysta')
    if artysta == 'q':
        break
    print("podaj tytuł płyty")
    print('Jeśli chcesz zakończyć napisz q')
    tytul = input("Podaj tytuł")
    if tytul == 'q':
        break

    cala_plyta = make_album(artysta, tytul)
    print(cala_plyta)

# ulubiona_plyta = make_album('republika', 'republika', liczba=11)
# print(ulubiona_plyta)


# def get_forrmated_name(first_name, last_name):
#     """Zwraca elegancko sformatowane pełne imie i nazwisko"""
#     full_name = f"{first_name} {last_name}"
#     return full_name
#
#
# while True:
#     print("Prosze podac imie i nazwisko: ")
#     print("Jeśli chcesz zakończyć wciśnij q")
#     f_name = input("Imie: ")
#     if f_name == "q":
#         break
#     l_name = input("Nawisko: ")
#     if l_name == "q":
#         break
#
#     formatted_name = get_forrmated_name(f_name, l_name)
#     print(formatted_name.title())
