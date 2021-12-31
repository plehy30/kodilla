def shopping():
    shopping_items = ["""
        "jajka",
        "bułka",
        "ser feta",
        "masło",
        "pomidor",
        "mleko"
        """
                      ]
    shopping_cart = "Mój koszyk zawiera: "
    for item in shopping_items:
        shopping_cart += item + "\n"
        return shopping_cart


print(shopping())


def day_times():
    return "morning", "afternoon", "evening", "night"


times = day_times()
print(times)
print(type(times))
jeden, dwa, trzy, cztery = day_times()
print("Trzeci element to %s" % trzy)


def customized_hell(first_name, last_name):
    print("Witaj", first_name, last_name)


customized_hell("Tomasz", "Leczkowski")

shopping_items = [
    "jajka",
    "bułka",
    "ser feta",
    "masło",
    "pomidor",
]

shopping_items.append("chusteczki")
shopping_items.append("papier toaletowy")


def shopping(items, payment="card", shop="local"):
    pass
    # shopping_card = "Koszyk zawiera: "
    # for item in items:
    #     shopping_card += item + "\n"
    # return shopping_card


# basket = shopping(shopping_items)
# print(basket)
shopping(shopping_items, payment="card")
