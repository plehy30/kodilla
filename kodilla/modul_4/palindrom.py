txt = str(input("Podaj słowo:"))


def palindrom1(txt):
    txt2 = txt.lower()
    txt2 = ''
    for znak in txt2:
        if znak.isalnum():
            txt = txt + znak
    if txt == txt[::-1]:
        return True
    return False


print(palindrom1(txt))


