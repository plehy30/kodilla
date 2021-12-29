# Damonstruje tworzenia krotek

# Utwórz pustą krotkę
inventory = ()

# Potraktuj krotkę jako warunek
if not inventory:
    print("Nie posiadasz niczego")

input("\nAby kontynuować misję naciśnij klawisz enter.")

# Utwórz krotę zawierającą pewnw elementy
inventory = ("miecz", "zbroja", "tarcza", "napój")
# Wyświetl krotkę
print("\nWykaz zawartości krotki: ")
print(inventory)
# Wyświetl każdy element krotki
print("\nElementy twojego wyposażenia: ")
for item in inventory:
    print(item)

input("\nAby zakończyć naciśnij Enter")
