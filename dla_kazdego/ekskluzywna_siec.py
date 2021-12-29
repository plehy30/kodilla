print("\tEksluzymna sieć komputerowa")
print("\t   Tylko dla członków")
security = 0
username = ""
while not username:
    username = input("Użytkownik: ")
password = ""
while not password:
    password = input("Hasło: ")
if username == "tomek" and password == "sekret":
    print("cześć Tomek")
    security = 5
elif username == "leszek" and password == "cywilizacja":
    print("cześć Leszek")
    security = 3
elif username == "andrzej" and password == "andrzejki":
    print("cześć Andrzej")
    security = 3
elif username == "zbyszek" and password == "zbychu":
    print("cześć Zbyszek")
    security = 3
elif username == "gosc" or password == "gosc":
    print("Witaj gościu")
    security = 1
else:
    print("Błąd\n")
    input("\n\nAby zakończyć prgram wciśnij Enter.")
