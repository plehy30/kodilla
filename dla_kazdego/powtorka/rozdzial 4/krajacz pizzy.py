# Demonstruje tworzenie wycinków łańcucha

slowo = "pizza"
print(
    """
    Ściągawka tworzenia wycinków
    
        0   1   2   3   4   5
        +---+---+---+---+---+
        | p | i | z | z | a |
        +---+---+---+---+---+
        -5 -4  -3  -2  -1
    """
)
print("Wprowadź poczatkowy i końcowy indeks wycinka łańcucha 'pizza'")
print("Aby zakończyć tworzenie wycinków, w odpowiedzi na monit 'Początek: ' naciśnij klawisz enter")
start = None
while start != "":
    start = (input("Wprowadź indeks początkowy: "))
    if start:
        start = int(start)

        koniec = int(input("Koniec: "))
        print("slowo[", start, ":", koniec, "] to", end=" ")
        print(slowo[start:koniec])

input("\nAby zakończyć naciśnij enter")
