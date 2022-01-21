class Cars():
    listaVin = []

    def __init__(self, marka, model, vin, stan, poj, cena):
        self.marka = marka
        self.model = model
        if vin in Cars.listaVin:
            raise Exception("Niepoprawny VIN")
        self.vin = vin
        Cars.listaVin.append(vin)
        self.stan = stan
        self.poj = poj
        self.cena = cena

    def __str__(self):
        return self.marka + " " + self.model + " " + self.stan

    def sam(self):
        return f"Marka:{self.marka}, model: {self.model}, vin:{self.vin}, stan:{self.stan}, pojemność:{self.poj}, max prędkość:{self.speed}, cena:{self.cena}"

    @property  # dynamiczny parametr
    def speed(self):
        return (self.poj / 10) * 2


car1 = Cars("ford", "Ka", 123456789, "nowy", 1200, 60000)
print(car1.sam())
car2 = Cars("mazda", "127", 223456789, "zadbany", 2000, 100000)
print(car2.sam())
car3 = Cars("Opel", "astra", 234563112, "uszkodzony", 1600, 10000)
car4 = Cars("Volvo", "S60", 345789871, "nowy", 2500, 160000)
car5 = Cars("Audi", "A4", 576876352, "zadbany", 2000, 50000)
samochody = [car1, car2, car3, car4, car5]
for car in samochody:
    print(car.sam())
zadbane = []
for car in samochody:
    if car.stan == 'zadbany':
        zadbane.append(car)
zadbane.sort(key=lambda car: car.cena, reverse=True)
for car in zadbane:
    print(car)
