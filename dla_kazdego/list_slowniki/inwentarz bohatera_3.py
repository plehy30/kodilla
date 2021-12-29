# Demonstruje listy

# utwórz listę zawierającą jakieś elementy
inwentarz = ["miecz", "zbroja", "tarcza", "napój"]
# wyświetl każdy element listy
print("Elementy twojego wyposażenia: ")
for item in inwentarz:
    print(item)
# wyświetl długość listy
print("Twój dobytek zawiera: ", len(inwentarz), " elementów")
# sprawdź czy element należy do listy
if "napój" in inwentarz:
    print("Dożyjesz bo masz napój")
# wyświetl jeden element wskazany przez indeks
index = int(input("\nWprowadź numer indeksu: "))
print("Pod indeksem ", index, " znajduje się: ", inwentarz[index])
# wyświetl wycinek
start = int(input("\nWprowadź indeks wyznaczający początek wycinka: "))
koniec = int(input("\nWprowadź indeks wyznaczający koniec wycinka: "))
print("inwentarz[", start, ":", koniec, "] to ", end=" ")
print(inwentarz[start:koniec])
# dokonaj konkatenacji dwóch list
skarb = ["złoto", "klejnoty"]
print("Znajdujesz skrzynię, która zawiera:")
print(skarb)
print("Dodajesz zawartość skrzyni do swojego inwentarza.")
inwentarz += skarb
print("Twój aktualny inwentarz to:")
print(inwentarz)
# przypisz poprzez index
print("Wymieniasz swój miecz na kuszę.")
inwentarz[0] = "kusza"
print("Twój aktualny inwentarz to:")
print(inwentarz)
# przypisz poprzez wycinek
print("Zużywasz swoje złoto i klejnoty na zakup kuli do wróżenia.")
inwentarz[4:6] = ["kula", "kula2"]
print("Twój aktualny inwentarz to:")
print(inwentarz)
# usuń element
print("W wielkiej bitwie Twoja tarcza zostaje zniszczona.")
del inwentarz[2]
print("Twój aktualny inwentarz to:")
print(inwentarz)
# usuń wycinek
print("Tawoja kusza i zbroja zostały skradzione przez złodziei.")
del inwentarz[:2]
print("Twój aktualny inwentarz to:")
print(inwentarz)
input("\nAby zakończyć naciśnij enter")
