# Twoim zadaniem jest zmodyfikowanie listy przypisanej do zmiennej numbers
# w taki sposób, aby każdy jej element zaokrąglić do pełnej dziesiątki.
# Postaraj się nie tworzyć nowej listy będącej zmodyfikowaną listą numbers,
# lecz zmodyfikować listę numbers.
#
# Po zaokrągleniu każdego elementu listy numbers, pozbądź się jej największego
# oraz najmniejszego elementu, a następnie do zmiennej mean_number
# przypisz średnią z ostatecznie zmodyfikowanej listy.
#
# Podsumowując: zaokrąglij każdy element numbers do pełnej 10 (np. 5 -> 10, 32 -> 30)
# znajdź, a następnie pozbądź się największego oraz najmniejszego elementu zmodyfikowanej listy
# policz średnią z ostatecznie zmodyfikowanej listy numbers i przypisz ją do zmiennej mean_number

numbers = [5, 32, 56, 2, 2, 16, 7, 10, 23, 100]
mean_number = 0


def zaokr(n):
    c = n % 10
    if c <= 4:
        n -= c
    else:
        n += (10 - c)
    return n


print(numbers)

# for i in range(len(numbers)):
#     numbers[i] = zaokr(numbers[i])
numbers = list(map(zaokr, numbers))

print(numbers)

numbers.remove(min(numbers))
numbers.remove(max(numbers))
print(numbers)

srednia = sum(numbers) / len(numbers)
mean_number = srednia
print(mean_number)
