class BaseCards:
    def __init__(self, name, last_name, company, standing, e_mail):
        self.name = name
        self.last_name = last_name
        self.company = company
        self.standing = standing
        self.e_mail = e_mail

    def __str__(self):
        return f'{self.name} {self.last_name} {self.company} {self.standing} {self.e_mail} '


person1 = BaseCards("Tomasz", 'Leczkowski', "szkola", 'nauczyciel', 'person1@gmail.com')
person2 = BaseCards('Tymoteusz', 'Kowalczyk', 'Auto Palace', 'Criminal investigator', 'TymoteuszKowalczyk@rhyta.com')
person3 = BaseCards('Róża', 'Kozłowska', 'Weingarten', 'Braille clerk', 'RozaKozlowska@rhyta.com')
persons = [person1, person2, person3]
print(persons)
by_name = sorted(persons, key=lambda person: person.name)
print(by_name)

print(person1)
