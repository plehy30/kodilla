# Translator slangu komputerowego
# Demonstruje używanie słowników

geek = {"404": "ignorant; od używanego w sieci WWW komunikatu o błędzie 404\n - nie znaleziono strony.",
        "Googling": "googlowanie; wyszukiwanie w internecie informacji dotyczących jakiejś osoby.",
        "Keyboard Plaque": "(skojarzone z kamieniem nazębnym)zanieczyszczenia nagromadzone w klawiaturze komputera.",
        "Link Rot": "(obumieranie linków) proces, w  wyniku którego linki do stron WWW stają się nieaktualne.",
        "Percussive Maintenance": "(konserwacja perkusyjna)naprawa urządzenia elektronicznego przez stuknięcie.",
        "Uninstalled": "(odinstalowany) zwolniony z pracy;  termin szczególnie popularny w okresie bańki internetowej."}
wybor = None
while wybor != "0":
    print(
        """
        Translator slangu komputerowego

        0 - zakończ
        1 - znajdź termin
        2 - dodaj nowy termin
        3 - zmień definicję terminu
        4 - usuń termin
        """
    )
    wybor = input("Wybierasz: ")
    print()
    if wybor == "0":
        print("Kończymy")
    elif wybor == "1":
        termin = input("Podaj termin jaki mam wyświetlić: ")
        if termin in geek:
            definicja = geek[termin]
            print("\n", termin, " oznacza: ", definicja)
        else:
            print("Nie ma takiego terminu")
    elif wybor == "2":
        termin = input("Jaki termin mam dodać? ")
        if termin not in geek:
            definicja = input("Podaj definicję: ")
            geek[termin] = definicja
            print("\n", termin, "został dodany")
        else:
            print("Taki termin już istnieje")
    elif wybor == "3":
        termin = input("Jaki termin mam przedefiniować? ")
        if termin in geek:
            definicja = input("Podaj defininicję: ")
            geek[termin] = definicja
            print("\n", termin, " został przedefiniowany.")
        else:
            print("Nie ma takiego terminu")
    elif wybor == "4":
        termin = input("Jaki termin mam usunąć? ")
        if termin in geek:
            del geek[termin]
            print("\n", termin, " został usuniety")
        else:
            print("Terminu nie ma w słowniku")
    else:
        print("nieprawidłowy wybór")

input("\n\nAby zakończyć naciśnij enter")
