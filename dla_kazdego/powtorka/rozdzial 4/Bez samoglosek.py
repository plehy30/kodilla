# Demonstruje tworzenie nowych łańcuchów przy użyciu pętli for
komunikat = input("Wprowadź komunikat: ")
nowy_komunikat = ""
SAMOGLOSKI = "aąeęioóuy"

for letter in komunikat:
    if letter.lower() not in SAMOGLOSKI:
        nowy_komunikat += letter
print("Nowy komunikat to: ", nowy_komunikat)
input("\nJeżeli chcesz zakończyć naciśnij enter")
