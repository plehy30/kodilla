txt = str(input("Podaj słowo:"))


def palindrom1(txt):
    txt = txt.lower()
    if txt == txt[::-1]:
        return True
    return False

print(palindrom1(txt))