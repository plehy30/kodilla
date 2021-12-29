# Zadanie 2
liczby = [1, 2, 3, 5, 6, 11, 12, 18, 19, 21]
pierwsze_sort = []

for liczba in liczby:
    if liczba >= 2:
        for i in range(2, liczba):
            if liczba % i == 0:
                break
        else:
            pierwsze_sort.append(liczba)

print(pierwsze_sort)
# Zadanie 1
name_list = ["John", "Michael", "Terry", "Eric", "Graham"]
print(name_list)
name_dictionary = {}
for name in name_list:
    name_dictionary[name] = len(name)
print(name_dictionary)
imiona_2 = []
for name in name_list:
    imiona_2.append(name)
print(imiona_2)

# Cwiczenie
names = ['Paweł', 'Kewin', 'Ireneusz', 'Bolesław', 'Mateusz', 'Edward', 'Piotr', 'Jan', 'Denis', 'Amir',
         'Igor', 'Borys', 'Robert', 'Ariel', 'Kuba', 'Rafał', 'Mateusz', 'Emanuel', 'Alfred', 'Artur', 'Jakub',
         'Ludwik', 'Bolesław', 'Remigiusz', 'Martin', 'Dobromił', 'Mariusz', 'Amadeusz', 'Łukasz', 'Bolesław', 'Amir',
         'Artur', 'Albert', 'Olgierd', 'Alek', 'Kordian', 'Julian', 'Anastazy', 'Emanuel', 'Józef']

name_dict = {}
for name in names:
    pierwsza_litera = name[0]
    if pierwsza_litera in name_dict:
        name_dict[pierwsza_litera].add(name)
    else:
        name_dict[pierwsza_litera] = {name}
# for name in names:
#     v = name_dict.setdefault(name[0], set())
#     v = v | {name}
#     name_dict[name[0]] = v
print(name_dict)
# Cwiczenie
num = 30
fibonacci = []
n = 1
while len(fibonacci) < num:
    if n == 1 or n == 2:
        fibonacci.append(1)
    else:
        fibonacci.append(sum(fibonacci[-2:]))
    n = n + 1
# while len(fibonacci) < num:
#     if n == 1 or n == 2:
#         fibonacci.append(1)
#     else:
#         fibonacci.append(sum(fibonacci[-2:]))
#     n = n + 1
print(fibonacci)

# Cwiczenie
exam_points = {
    "Mariusz": 30,
    "Mateusz": 55,
    "Marta": 76,
    "Roman": 30,
    "Arleta": 59,
    "Adrian": 96,
    "Monika": 91,
    "Andrzej": 22,
    "Krzysztof": 83,
    "Krystyna": 93,
    "Piotr": 44,
    "Dawid": 10,
    "Agnieszka": 15
}

failed_students = []
top_students = []
best_student = ("", 0)
max_score = 0
for student, score in exam_points.items():
    if score <= 45:
        failed_students.append(student)
    elif score >= 91:
        top_students.append(student)
    while score > max_score:
        max_score = score
        best_student = (student, score)

# for student, score in exam_points.items():
#     if score <= 45:
#         failed_students.append(student)
#     elif score >= 91:
#         top_students.append(student)
#
#     if score > max_score:
#         max_score = score
#         best_student = (student, score)

print(failed_students)
print(top_students)
print(best_student)
