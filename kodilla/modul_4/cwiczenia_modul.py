def shopping():
    shopping_items = ["jajka", "bułki", "masło"]
    shopping_cart = "Koszyk zawiera: "
    for item in shopping_items:
        shopping_cart += item + "\n"
    return shopping_cart


print(shopping())
