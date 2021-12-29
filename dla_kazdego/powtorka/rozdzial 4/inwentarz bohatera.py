# Demonstruje tworzenie krotek
# Utwórz pusta krotkę

inwentarz = ()
# potraktuj krotkę jako warunek

if not inwentarz:
    print("Nie masz nic")

input("\nAby kontynuować misję naciśnij enter")
# utwórz krotkę zawierającą jakieś elementy
inwentarz = ("miecz", "zbroja", "tarcza", "napój")
# wyświetl każdy element krotki
print("Elementy twojego wyposażenia: ")
for item in inwentarz:
    print(item)
print("Twój dobytek zawiera ", len(inwentarz), " elementów")
if "napój" in inwentarz:
    print("Przeżyjesz")
# Wyświetl wycinek
start = int(input("początek indeksu: "))
koniec = int(input("koniec indeksu: "))
print(inwentarz[start:koniec])
input("\nAby zakończyć naciśnij enter")
