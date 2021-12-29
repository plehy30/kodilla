wiadomosc = input("Wprowadź wiadomość: ")
new_wiad = ""
polskie = "aąeęioóuy"
print()
for letter in wiadomosc:
    if letter.lower() not in polskie:
        new_wiad += letter
        print("Został utworzony nowy łańcuch: ", new_wiad)
print("\nTwój komunikat bez samogłosek to: ", new_wiad)
input("\n\nAby zakończyć program naciśnij Enter.")
