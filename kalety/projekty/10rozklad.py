# rozkład liczby na czynniki pierwsze

def rozklad(x):
    wynik = []
    while x % 2 == 0:
        wynik.append(2)
        x //= 2
    r = 3
    while r * r <= x:
        while x % r == 0:
            wynik.append(r)
            x //= r
        r += 2
    if x > 1:
        wynik.append(x)
    return wynik


while 1:
    x = int(input('x='))
    if x < 1:
        break
    print(f"{x}: {rozklad(x)}")
