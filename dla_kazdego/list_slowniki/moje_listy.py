lista = ["stol", "krzeslo", "komputer"]
print(lista)
wybor = None
while wybor != "":
    wybor = input("Twoj wybór: ")
    if wybor == "0":
        print("Twoja lista: ", lista)
    elif wybor == "1":
        element = input("Podaj element listy: ")
        lista.append(element)
    elif wybor == "2":
        element = input("Podaj element do usunięcia: ")
        if element in lista:
            lista.remove(element)
        else:
            print("Nie ma takiego elementu")
