vegetables = ["burak", "ziemniak", "szczypior", "cebula"]
for vegetable in vegetables:
    print(vegetable)
veggie_iterator = iter(vegetables)
print(veggie_iterator)
for vegetable in veggie_iterator:
    print(vegetable)
warzywa_iterator = iter(vegetables)
print(next(warzywa_iterator))
print(next(warzywa_iterator))
print(next(warzywa_iterator))
print(next(warzywa_iterator))

shopping = [("buraki", 1.25), ("mleko", 4.0), ("chleb", 3.50), ("wino", 15)]
for produkt, price in shopping:
    print(produkt, price)
shopping_slownik = dict(shopping)
print(shopping_slownik)
for produkt in shopping_slownik:
    print(produkt)
for produkt in shopping_slownik.items():
    print(produkt)
