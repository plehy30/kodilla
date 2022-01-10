class BaseCard:

    def __init__(self, imie, tel):
        self.imie = imie
        self.tel = tel

    @property  # atrybut dynamiczny
    def contact_phone(self):
        return self.tel

    def contact(self):
        return f"Dzwonie do {self.imie} pod numer {self.contact_phone}"

    def label_length(self):
        return len(f"{self.imie} {self.contact_phone}")


class BusinessCard(BaseCard):

    def __init__(self, imie, tel, tel_prac):
        super().__init__(imie, tel)
        self.tel_prac = tel_prac

    @property
    def contact_phone(self):
        return self.tel_prac
