greetings = "Witaj świecie"
greetings_type = type(greetings)
print(greetings_type)
name = "Tomek"
age = 50
personalized_greetings = "Twoje imię: %s, masz lat %d" % (name, age)
f_personalized_greetings = f"Witaj {name}, masz lat {age}"
print(personalized_greetings)
print(f_personalized_greetings)
print(int("1") + int("1"))
print(3 * 3)
print(3 ** 3)
print(28 / 3)
print(28 // 3)
print(28 % 3)
for i in range(10):
    print("Hej")
for i in range(1, 12):
    print(i)
word = "Kodilla"
for letter in word:
    print(letter)
for year in range(2020, 2021):
    for month in range(1, 13):
        print("Rok " + str(year))
        print("Miesiąc " + str(month))
for i in range(6):
    print("*" * i)
for i in range(5):
    print("* " * 10)
    print(" " + "* " * 10)
for i in range(2, 9, 2):
    print("* " * i)
    print("* " * i)
for i in range(7, 0, -1):
    print("*" * i)
my_bool = True
print(my_bool)
print(type(my_bool))
print(bool(0.1))  # true
print(bool(1))
print(bool(-1))
print(bool(0.0))  # false
print(bool(0))  # false
print(bool(""))  # false
print(bool(''))  # false
print(bool(" "))  # true
print(bool('false'))
raining = True
if raining:
    print("Biorę parasol")
else:
    print("nie biorę")
available_cheese = 'brie'
if available_cheese == "edam":
    print("Kupuję edam")
elif available_cheese == "brie":
    print("Kupuję brie")
else:
    print("Kupuję goudę")

number = 3
while number > 0:
    print(number)
    number = number - 1
number = 5
for i in range(1, 10):
    print(i)
    if i > 5:
        print("Wychodzimy")
        break
for i in range(1, 10):
    print(i)
    if i > 5:
        continue
    print("Działamy jeszcze raz")
greetings = "witaj świecie"
print(greetings)
type_greetings = type(greetings)
print(type_greetings)
name = "Tomek"
age = 51
personalizet_name = "Witaj %s, lat %d" % (name, age)
personalizet_name_f = f"Witaj {name}, lat {age}"
print(personalizet_name)
print(personalizet_name_f)
for i in range(1, 11, -1):
    print(i)
