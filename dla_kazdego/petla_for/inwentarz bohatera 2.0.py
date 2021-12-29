# Demonstruje krotki
# Utwórz krotkę zawierającą pewne elementy i wyświetl jej zawartość za pomocą pętli for
inventory = ("miecz", "zbroja", "tarcza", "napój")
print("\nTwój inwentarz: ")
for item in inventory:
    print(item)

# Wyświetl długość krotki
print("Twój dobytek zawiera ", len(inventory), "elementów.")
# sprawdź czy element należy do krotki za pomocą in
if "napój" in inventory:
    print("Dożyjesz dnia")
# wyświetl jeden element wskazany przez index
index = int(input("\nWprowadź numer indeksu inwentarza"))
print("\nPod indeksem ", index, "znajduje się ", inventory[index])
# dokonaj konkatenacji  dwóch krotek
krotka=("złoto", "srebro")
print("\nDodajesz: ", krotka)
inventory+=krotka
print("\nTeraz twój inwentarz to: ", inventory)

input("\nAby zakończyć naciśnij Enter.")
