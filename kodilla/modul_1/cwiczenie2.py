for i in range(11, 0, -1):
    print(i)
powtorzenia = 0
n = 0
while powtorzenia <= 30:
    if n % 6 == 0:
        print(n)
    powtorzenia = powtorzenia + 1
    n += 6
# for i in range(1, 100):
#  if i % 3 == 0:
#     print(i)

i = 0
while True:
    if i == 100:
        break
    if i % 3 == 0:
        print(i, end=" ")
    i += 1
