# inventory = ["miecz", "zbroja", "tarcza", "napoj"]
# print(" moje uzbrojenie: ")
# for item in inventory:
#     print(item)
# print("Twój dobytek zawiera ", len(inventory), " elementów")
# if "napoj" in inventory:
#     print("przeżyjesz")
# # index = int(input("Wprowadż numer indeksu: "))
# # print("Pod indeksem: ", index, "zanajduje się: ", inventory[index])
# # # wyświetl wycinek
# # start = int(input("Wprowadź indeks początku wycinka: "))
# # koniec = int(input(" Wprowadź indeks końca wycinka: "))
# # print("inventory[", start, ":", koniec, "]to", end=" ")
# # print(inventory[start:koniec])
# chest = ["złoto", "klejnoty"]
# inventory += chest
# print(inventory)
# inventory[0]="kusza"
# print(inventory)
# inventory[1:3]=["kula"]
# print(inventory)
wyniki = []
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
    if wybor == "0":
        print("Kończymy")
    elif wybor == "1":
        print("Najlepsze wyniki\n")
        print("Gracz\tWynik")
        for entry in wyniki:
            punkty, name = entry
            print(entry)
    elif wybor == "2":
        name = input("Podaj imię: ")
        punkty = int(input("Podaj wynik: "))
        entry = (punkty, name)
        wyniki.append(entry)
        wyniki.sort(reverse=True)
        wyniki = wyniki[:5]  # zachowaj tylko 5 najlepszych wyników
        print(wyniki)
    # elif wybor == "3":
    #     punkt = int(input("Podaj numer do usunięcia: "))
    #     if punkt in wyniki:
    #         wyniki.remove(punkt)
    #     else:
    #         print(" Nie ma takiego numeru")
    #     print(wyniki)
    # elif wybor == "4":
    #     wyniki.sort(reverse=True)
    #     print(wyniki)
    else:
        print("Nie ma takiego wyboru")
# scores=[("piotr","100"),("tomek","200")]
# print(scores[1][0])
