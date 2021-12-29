# Demonstruje operatory logiczne i warunki złożone
print("Wejście tylko dla wybranych, \n wpisz swój login i hasło")
login = ""
while not login:
    login = input("Login: ")
haslo = ""
while not haslo:
    haslo = input("Hasło: ")

if login == "plehy" and haslo == "basic1":
    print("Zapraszam")
elif login == "tomek" and haslo == "basic123":
    print("Zapraszam")
elif login == "login" or haslo == "haslo":
    print("Nie koniecznie")
else:
    print("Niestety nie")
input("\nAby zakończyć naciśnij enter")
