# demonstruje metody listy
punkty = []
wybor = None
while wybor != "0":
    print(
        """
        Najlepsze wyniki

        0 - zakończ
        1 - pokaż wyniki
        2 - dodaj wynik
        3 - usuń wynik 
        4 - posortuj wyniki
        """
    )
    wybor = input("Wybierasz: ")
    print()
    # Zakończ program
    if wybor == "0":
        print("Do widzenia")
    # wypisz tabele najlepszych wyników
    elif wybor == "1":
        print("Najlepsze wyniki")
        for punkt in punkty:
            print(punkt)
    # dodaj wynik
    elif wybor == "2":
        punkt = int(input("Jaki wynik uzyskałeś?: "))
        punkty.append(punkt)
    # usuń wynik
    elif wybor == "3":
        punkt = int(input("Który wynik usunąć?: "))
        if punkt in punkty:
            punkty.remove(punkt)
        else:
            print("Nie ma takiego wyniku")
    # posortuj wyniki
    elif wybor == "4":
        punkty.sort(reverse=True)
        print(punkty)
    # nieznana opcja
    else:
        print("Niestety nie istnieje taki wybór: ", wybor)

input("\nJeżeli chcesz zakończyć naciśnij enter")
