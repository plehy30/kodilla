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
        """
    )
    wybor = input("Wybierasz: ")
    print()
    # Zakończ program
    if wybor == "0":
        print("Do widzenia")
    # wyświetl tabelę najlepszych wyników
    elif wybor == "1":
        print("Najlepsze wyniki\n")
        print("GRACZ\tWYNIK")
        for entry in punkty:
            punkt, name = entry
            print(name, "\t", punkt)
    # dodaj wynik
    elif wybor == "2":
        name = input("Podaj nazwę gracza: ")
        punkt = int(input("Jaki wynik uzyskał gracz?: "))
        entry = (punkt, name)
        punkty.append(entry)
        punkty.sort(reverse=True)
        punkty = punkty[:5]  # zachowaj tylko 5 najlepszych wyników
    else:
        print("Niestety ", wybor, " nie jest prawidłowym wyborem.")
input("\nJeżeli chcesz zakończyć naciśnij enter")
