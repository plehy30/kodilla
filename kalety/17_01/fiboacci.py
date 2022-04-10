def fib_r(n):
    if n <= 2:
        return 1
    else:
        return fib_r(n - 1) + fib_r(n - 2)


def fib_i(n):
    if n <= 2:
        return 1
    else:
        fa, fb = 1, 1
        for i in range(2, n):
            f = fa + fb
            fb = fa
            fa = f
        return f


n = int(input("Podaj n "))
print(fib_i(n))
print(fib_r(n))
