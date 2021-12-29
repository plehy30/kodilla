chees1 = "roquefort"
chees1_price = float(12.50)
chees1_weight = 2
chees2 = "stilton"
chees2_price = 11.24
chees3 = "brie"
chees3_price = 9.30
chees4 = "gouda"
chees4_price = 8.55
chees5 = "edam"
chees5_price = 11
chees6 = "parmezan"
chees6_price = 16.50
chees6_weight = 3.5
chees7 = "mozzarella"
chees7_price = 14
chees7_weight = 0.13
chees8 = "ser z owczego mleka"
chees8_price = 122.32
chees8_weight = 0.22
mint = "listek miętowy"
mint_price = 20
mint_weight = 0.2
zakupy = f"Raport z zakupów: \n" \
         f"{chees1:<19}, {chees1_weight:^5.2f}kg za {(chees1_price) * (chees1_weight):^5.2f} złotych\n" \
         f"{chees6:<19}, {chees6_weight:^5.2f}kg za {(chees6_price) * (chees6_weight):^5.2f} złotych \n" \
         f"{chees7:<19}, {chees7_weight:^5.2f}kg za {(chees7_price) * (chees7_weight):^5.2f} złotych\n" \
         f"{chees8:<19}, {chees8_weight:^5.2f}kg za {(chees8_price) * (chees8_weight):^5.2f} złotych \n" \
         f"{chees2:<19}, 1 kg za {chees2_price} złotych \n" \
         f"{mint:<19}, {mint_weight:^5.2f}kg za {(mint_price) * (mint_weight):^5.2f} złote \n" \
         f"{chees3:<19}, 1 kg za {chees3_price} złotych \n" \
         f"{chees4:<19}, 1 kg za {chees4_price} złotych \n" \
         f"{chees5:<19}, 1 kg za {chees5_price} złotych \n"
suma = ((chees1_price * chees1_weight) + (chees6_weight * chees6_price) + (chees7_price * chees7_weight) + (
            chees8_price * chees8_weight) + (mint_weight * mint_price)
        + chees2_price + chees3_price + chees4_price + chees5_price)
print(zakupy)
print("Za wszystko zapłaciłem: ", f"{suma:.2f}", " złotych")
