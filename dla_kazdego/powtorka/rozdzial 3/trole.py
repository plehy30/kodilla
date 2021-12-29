# demonstruje pętle nieskończoną
zycie = 10
trole = 0
zdrowie = 3

while zycie > 0:
    trole += 1
    zycie -= zdrowie
    print("Bohater pokonał trola ale stracił ", zdrowie, " punkty z zycia")
print("Zginął ale zabił ", trole, "troli")

input("\nAby zakończyć naciśnij enter")
