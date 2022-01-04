import math

print(math.pi)
s = 'mielonka'
print(len(s))
print(s[2])
s = 'z' + s[1:]
print(s)

L = [[123, 'mielonka', 1.23],
     [1, 2, 3, 4],
     [5, 6, 7]]
print(L[2][2])
x = 4
while x > 0:
    print('mielonka' * x)
    x -= 1

D = {'a': 1, 'b': 2, 'c': 3}

Ks = list(D.keys())
print(Ks)

for key in sorted(D):
    print(key, ' => ', D[key])

l = [1, 2, 3, 4]
del l[1:]
print(l)
me={'name':('Robert','F','Zielony'),'age':'?','job':'inżynier'}
print(me['job'])
print(me['name'][2])
