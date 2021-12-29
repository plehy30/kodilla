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
