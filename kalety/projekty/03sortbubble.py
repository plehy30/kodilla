tab = [33, 22, 44, 77, 11, 66, 88, 55, 99, 0]


# ---------------------------------------------
def pisz(tt, opis=""):
    for x in tt:
        print(x, end=" ")
    print(opis)


# ---------------------------------------------
# Sortowanie bąbelkowe (BUBBLE)
# ---------------------------------------------
def sortuj(tt):
    n = len(tt)
    for m in range(n - 1, 0, -1):
        for i in range(0, m):
            if tt[i] > tt[i + 1]:
                pom = tt[i]
                tt[i] = tt[i + 1]
                tt[i + 1] = pom
        pisz(tt, "   m=" + str(m))


# ---------------------------------------------
pisz(tab, "   Tablica oryginalna")
print("-------------------------------------------------------")
sortuj(tab)
print("-------------------------------------------------------")
pisz(tab, "   Tablica posortowana")
