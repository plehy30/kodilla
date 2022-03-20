import math


class Ulamek:
    def __init__(self, licznik, mianownik=1):
        self.li = licznik
        self.mi = mianownik
        self.normalizacja()

    def __str__(self):
        return f"({self.li} / {self.mi})"

    def __int__(self):
        return self.li // self.mi

    def __float__(self):
        return self.li / self.mi

    def __format__(self, d):
        if d == "":
            return str(self)
        elif d[-1] == "d":
            return str(self.li / self.mi)

    def normalizacja(self):  # skracanie
        if self.mi < 0:
            self.li, self.mi = -self.li, -self.mi
        nwd = math.gcd(self.li, self.mi)
        self.li //= nwd
        self.mi //= nwd

    @staticmethod
    def toulamek(x):
        u = x
        if isinstance(x, int):
            u = Ulamek(x)
        if isinstance(x, float):
            u = Ulamek(int(x * 1e10), 10000000000)
        u.normalizacja()
        return u

    @staticmethod
    def add(a, b):
        ll = a.li * b.mi
        pl = a.mi * b.li
        wynik = Ulamek(ll + pl, a.mi * b.mi)
        wynik.normalizacja()
        return wynik

    @staticmethod
    def sub(a, b):
        ll = a.li * b.mi
        pl = a.mi * b.li
        wynik = Ulamek(ll - pl, a.mi * b.mi)
        wynik.normalizacja()
        return wynik

    @staticmethod
    def mul(a, b):
        wynik = Ulamek(a.li * b.li, a.mi * b.mi)
        wynik.normalizacja()
        return wynik

    @staticmethod
    def div(a, b):  # operator /
        wynik = Ulamek(a.li * b.mi, a.mi * b.li)
        wynik.normalizacja()
        return wynik

    def __add__(self, x):
        return Ulamek.add(self, Ulamek.toulamek(x))

    def __sub__(self, x):
        return Ulamek.sub(self, Ulamek.toulamek(x))

    def __mul__(self, x):
        return Ulamek.mul(self, Ulamek.toulamek(x))

    def __truediv__(self, x):
        return Ulamek.div(self, Ulamek.toulamek(x))

    def __radd__(self, x):
        return Ulamek.add(Ulamek.toulamek(x), self)

    def __rsub__(self, x):
        return Ulamek.sub(Ulamek.toulamek(x), self)

    def __rmul__(self, x):
        return Ulamek.mul(Ulamek.toulamek(x), self)

    def __rtruediv__(self, x):  # operator /
        return Ulamek.div(Ulamek.toulamek(x), self)

    def __iadd__(self, x):
        u = Ulamek.add(self, Ulamek.toulamek(x))
        self.li, self.mi = u.li, u.mi
        return self

    def __isub__(self, x):
        u = Ulamek.sub(self, Ulamek.toulamek(x))
        self.li, self.mi = u.li, u.mi
        return self

    def __imul__(self, x):
        u = Ulamek.mul(self, Ulamek.toulamek(x))
        self.li, self.mi = u.li, u.mi
        return self

    def __itruediv__(self, x):
        u = Ulamek.div(self, Ulamek.toulamek(x))
        self.li, self.mi = u.li, u.mi
        return self


u1 = Ulamek(6, 7)
u2 = Ulamek(1, 2)
w1 = u1 + u2
w2 = u1 - u2
w3 = u1 * u2
w4 = u1 / u2

print(f"{u1} + {u2} = {w1}")
print(f"{u1} - {u2} = {w2}")
print(f"{u1} * {u2} = {w3}")
print(f"{u1} / {u2} = {w4}")
print(u1)
u1 += 1
print(f" po +=1 {u1}")
u1 += 1
print(f" po +=1 {u1}")
u1 *= 2
print(f" po *=2 {u1}")
u1 /= 3
print(f" po /=3 {u1}")
u1 += 1
print(f" po += {u1} {u1:.5d}")
