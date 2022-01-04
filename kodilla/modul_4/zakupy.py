def shopping(items, payment='card', shop="local"):
    result = ''
    result = result + "idę na zakupy do %s. \n" % shop
    result = result + "kupię następujące rzeczy:\n"
    for item in items:
        result = result + "-%s\n" % item
    result = result + "By zapłacić, używam %s." % payment
    return result


# items = ["cola", 'whiskey', 'lód']
# text = shopping(items, 'card', 'small local shop')
# print(text)
if __name__ == "__main__":
    items_next = input("Podaj produkty rozdzielone przecinkami:")
    items = items_next.split(',')
    shopping_resultat = shopping(items)
    print(shopping_resultat)
