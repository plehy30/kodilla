waluty = [{"table": "C", "no": "031/C/NBP/2022", "tradingDate": "2022-02-14", "effectiveDate": "2022-02-15",
           "rates": [{"currency": "dolar amerykaÅ„ski", "code": "USD", "bid": 3.9675, "ask": 4.0477},
                     {"currency": "dolar australijski", "code": "AUD", "bid": 2.8278, "ask": 2.8850},
                     {"currency": "dolar kanadyjski", "code": "CAD", "bid": 3.1164, "ask": 3.1794},
                     {"currency": "euro", "code": "EUR", "bid": 4.4912, "ask": 4.5820},
                     {"currency": "forint (WÄ™gry)", "code": "HUF", "bid": 0.012578, "ask": 0.012832},
                     {"currency": "frank szwajcarski", "code": "CHF", "bid": 4.2841, "ask": 4.3707},
                     {"currency": "funt szterling", "code": "GBP", "bid": 5.3698, "ask": 5.4782},
                     {"currency": "jen (Japonia)", "code": "JPY", "bid": 0.034343, "ask": 0.035037},
                     {"currency": "korona czeska", "code": "CZK", "bid": 0.1832, "ask": 0.1870},
                     {"currency": "korona duÅ„ska", "code": "DKK", "bid": 0.6035, "ask": 0.6157},
                     {"currency": "korona norweska", "code": "NOK", "bid": 0.4470, "ask": 0.4560},
                     {"currency": "korona szwedzka", "code": "SEK", "bid": 0.4238, "ask": 0.4324},
                     {"currency": "SDR (MFW)", "code": "XDR", "bid": 5.5163, "ask": 5.6277}
                     ]}]
rates = waluty[0]["rates"]  # lista słowników walut

kody = ""
for waluta in rates:
    kody = kody + waluta["code"] + " "

while True:
    kodwej = input(f"Podaj kod kraju ({kody} lub x (koniec)): ").upper()
    if kodwej == "X":
        exit(0)
    kod = ""
    for waluta in rates:
        if kodwej == waluta["code"]:
            kod = waluta["code"]
            break
    if kod == "":
        print(f"nieprawidłowy kod: {kod}")
    else:
        nazwa = waluta["currency"]
        kurs = waluta["ask"]
        kwota = float(input(f"Podaj kwotę w {nazwa}: "))
        kwota2 = kwota * kurs
        print(f"{kwota:.2f} {nazwa} --> {kwota2:.2f} złoty")
