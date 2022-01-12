class BaseCards:
    def __init__(self, name, last_name, company, standing, e_mail):
        self.name = name
        self.last_name = last_name
        self.company = company
        self.standing = standing
        self.e_mail = e_mail

    def __str__(self):
        return f'{self.name} {self.last_name} {self.company} {self.standing} {self.e_mail} '

    def contact(self):
        print(f'Kontaktuj się z {self.name} {self.last_name} {self.e_mail}')

    @property
    def dl_imie(self):
        return len(self.name) + len(self.last_name) + 1


class BusinessCard(BaseCards):
    def __init__(self, company, standing, phone):
        super().__init__(*company, **standing)
        self.phone = phone


person1 = BaseCards("Tomasz", 'Leczkowski', "szkola", 'nauczyciel', 'person1@gmail.com')
person2 = BaseCards('Tymoteusz', 'Kowalczyk', 'Auto Palace', 'Criminal investigator', 'TymoteuszKowalczyk@rhyta.com')
person3 = BaseCards('Róża', 'Kozłowska', 'Weingarten', 'Braille clerk', 'RozaKozlowska@rhyta.com')
persons = [person1, person2, person3]

for p in persons:
    print(f'{p.name} {p.last_name} {p.e_mail}')

persons.sort(key=lambda p: p.name, reverse=True)
print('Po posortowaniu: ')

for p in persons:
    print(f'{p.name} {p.last_name} {p.e_mail}')

print(person1.dl_imie)

person1.contact()
