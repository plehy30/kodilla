tab = [33, 22, 44, 77, 11, 66, 88, 55, 99, 10]


# ---------------------------------------------
def pisz(tt, opis=""):
    for x in tt:
        print(x, end=" ")
    print(opis)


# ---------------------------------------------
# Sortowanie przez wstawianie (INSERT)
# ---------------------------------------------
def sortuj(tt):
    n = len(tt)
    for i in range(1, n):
        j = i
        pom = tt[i]
        while tt[j - 1] > pom and j > 0:
            tt[j] = tt[j - 1]
            j -= 1
        tt[j] = pom
        pisz(tt, "   i=" + str(i))


# ---------------------------------------------
pisz(tab, "   Tablica oryginalna")
print("-------------------------------------------------------")
sortuj(tab)
print("-------------------------------------------------------")
pisz(tab, "   Tablica posortowana")
