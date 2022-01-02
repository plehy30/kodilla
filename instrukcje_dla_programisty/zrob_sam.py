def show_messages(wiadomosci):
    for wiadomosc in wiadomosci:
        print(wiadomosc)


def send_messages(wiadomosci, wyslane):
    while wiadomosci:
        wiadomosc = wiadomosci.pop()
        wyslane.append(wiadomosc)


wiadomosci = ['hej', 'czesc', 'sie ma']
wyslane = []
show_messages(wiadomosci)
send_messages(wiadomosci[:], wyslane)
print(wiadomosci)
print(wyslane)
