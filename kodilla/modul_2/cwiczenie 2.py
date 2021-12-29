names = ['Paweł', 'Kewin', 'Ireneusz', 'Bolesław', 'Mateusz', 'Edward', 'Piotr', 'Jan', 'Denis', 'Amir',
         'Igor', 'Borys', 'Robert', 'Ariel', 'Kuba', 'Rafał', 'Mateusz', 'Emanuel', 'Alfred', 'Artur', 'Jakub',
         'Ludwik', 'Bolesław', 'Remigiusz', 'Martin', 'Dobromił', 'Mariusz', 'Amadeusz', 'Łukasz', 'Bolesław', 'Amir',
         'Artur', 'Albert', 'Olgierd', 'Alek', 'Kordian', 'Julian', 'Anastazy', 'Emanuel', 'Józef']

name_dict = {}
for name in names:
    v = name_dict.setdefault(name[0], set())
    v = v | {name}
    name_dict[name[0]] = v
print(name_dict)
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
