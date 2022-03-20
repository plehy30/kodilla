#sortowanie przez wybieranie SELECT

tab = [33, 22, 44, 77, 11, 66, 88, 55, 99, 0]


# ---------------------------------------------
def pisz(tt, opis=""):
    for x in tt:
        print(x, end=" ")
    print(opis)


# ---------------------------------------------
# Sortowanie przez wybieranie (SELECT)
# ---------------------------------------------
def sortuj(tt):
    n = len(tt)
    for i in range(0, n - 1):
        mini = i
        for j in range(i + 1, n):
            if tt[j] < tt[mini]:
                mini = j
        pom = tt[mini]
        tt[mini] = tt[i]
        tt[i] = pom
        pisz(tt, "   i=" + str(i))


# ---------------------------------------------
pisz(tab, "   Tablica oryginalna")
print("-------------------------------------------------------")
sortuj(tab)
print("-------------------------------------------------------")
pisz(tab, "   Tablica posortowana")
