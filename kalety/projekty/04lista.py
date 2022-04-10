# operacje na liście

from functools import reduce

# def suma(lista):
#    w=0;
#    for x in lista:
#        w+=x
#    return w

# def iloczyn(lista):
#    w=1;
#    for x in lista:
#        w*=x
#    return w


def suma(ll):
    return reduce(lambda x, y: x + y, ll)


def iloczyn(ll):
    return reduce(lambda x, y: x * y, ll)


def dane():
    print("podaj listę liczb. Zakończenie - Enter")
    xx = []
    while True:
        x = input("x=")
        if x == "":
            break
        xx.append(int(x))
    return xx


lista = dane()
nx = len(lista)
ys = suma(lista)
ym = iloczyn(lista)

print("lista =", lista)
print(f"n = {nx}")
print(f"suma = {ys}")
print(f"iloczyn = {ym}")
