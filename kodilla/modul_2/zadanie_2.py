# Zadanie 2
liczby = [1, 2, 3, 5, 6, 11, 12, 18, 19, 21]
pierwsze_sort = []
n = 0
for liczba in liczby:
    if n == liczba:
        for i in range(n):
            if n % i == 0: break
        else:
            pierwsze_sort.append(n)
print(pierwsze_sort)

# Zadanie 3
dni = ["pon", "śro", "pią", "sob"]
dni.insert(1, "wto")
dni.insert(3, "czwa")
dni.append("nie")
print(dni)

# Zadanie 4

herbata_set = ["2. włącz czajnik", "4. znajdź opakowanie herbaty", "6. zalej herbatę",
               "1. nalej wody do czajnika", "3. wyjmij kubek", "5. włóż herbatę do kubka"]
herbata_set.sort()
print(herbata_set)
