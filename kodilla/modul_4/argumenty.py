print("Witaj w programie w którym na podstawie wieku powiem czy jesteś pełnoletni")
adult = None
sex = input('Podaj swoja płeć: M/K')
if sex == "M":
    age = int(input('Podaj swój wiek: '))
    adult = age >= 18
elif sex == "K":
    print("Kobiet o wiek się nie pyta więc zapytam sie inaczej")
    over18 = input("Czy miałaś już osiemnastkę")
    adult = (over18 == 'T')
else:
    print('Nie ma takiej płci')
    exit(1)

print("Twoja pełnoletność w boolean to %s" % str(adult))
