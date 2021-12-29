response = ""
while response != "Dlatego":
    response = input("Dlaczego?\n")

print("Już wiem")
zycia = 10
trole = 0
punkty = 3
while zycia > 0:
    trole += 1
    zycia -= punkty
    print("Pokonuje ale traci", punkty, "zycia")
