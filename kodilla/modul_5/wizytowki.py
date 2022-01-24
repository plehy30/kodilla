from faker import Faker

fake = Faker()
print(fake.name())


class BaseCards:
    def __init__(self, name, last_name, tel, company, standing, e_mail):
        self.name = name
        self.last_name = last_name
        self.tel = tel
        self.company = company
        self.standing = standing
        self.e_mail = e_mail

    def __str__(self):
        return f'{self.name} {self.last_name} {self.tel} {self.company} {self.standing} {self.e_mail} '

    @property  # atrybut dynamiczny
    def contact_phone(self):
        return self.tel

    def contact(self):
        return f"Dzwonie do {self.name} {self.last_name} pod numer {self.contact_phone}"

    @property
    def label_length(self):
        return len(f"{self.name} {self.last_name} {self.contact_phone}")


class BusinessCard(BaseCards):

    def __init__(self, name, last_name, tel, company, standing, e_mail, tel_prac):
        super().__init__(name, last_name, tel, company, standing, e_mail)
        self.tel_prac = tel_prac

    @property
    def contact_phone(self):
        return self.tel_prac

    def contact(self):
        return f"Dzwonie do {self.name} {self.last_name} pod numer {self.contact_phone}"


person1 = BaseCards("Tomasz", 'Leczkowski', "45678920", "szkola", 'nauczyciel', 'person1@gmail.com')
person2 = BaseCards('Tymoteusz', 'Kowalczyk', "345698721", 'Auto Palace', 'Criminal investigator',
                    'TymoteuszKowalczyk@rhyta.com')
person3 = BaseCards('Róża', 'Kozłowska', '1232454321', 'Weingarten', 'Braille clerk', 'RozaKozlowska@rhyta.com')
persons = [person1, person2, person3]
for p in persons:
    print(p)

persons.sort(key=lambda person: person.name)
for p in persons:
    print(p)
persons.sort(key=lambda person: person.last_name)
for p in persons:
    print(p)
persons.sort(key=lambda person: person.e_mail)
for p in persons:
    print(p)

print(person1)
print(person1.label_length)
