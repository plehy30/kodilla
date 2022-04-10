txt1 = "kajak"
print(txt1[0:])
print(txt1[2:])
print(len(txt1))
print(txt1[::-1])
#################################
x = 'ABCDEFGHIJK'
y = x[::-1]
print(y)

txt = str(input("Podaj zdanie:"))


def palindrom1(t):
    t = t.replace(" ", "").lower()
    if t == t[::-1]:
        return True
    return False


##################################
def palindrom2(t):
    t = t.replace(" ", "").lower()
    n = len(t)
    for i in range(0, n):
        j = n - 1 - i
        if i > j:
            break
        if t[i] == t[j]:
            i += 1
            j -= 1
            continue
        else:
            return False
    return True


print(palindrom1(txt))
print(palindrom2(txt))
