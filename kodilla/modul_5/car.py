class Car:
    def __init__(self, make, model_name, top_speed, color):
        self.make = make
        self.model_name = model_name
        self.top_speed = top_speed
        self.color = color

        self.current_speed=0

    def accererate(self, step=10):
        self.current_speed+=10

    def decelerate(self,step=10):
        self.current_speed+=-10

    def __str__(self):
        return f'{self.color} {self.model_name} {self.make}'

    def __repr__(self):
        return f'Car(make={self.make} model={self.model_name} top_speed={self.top_speed} color={self.color}'

    def __gt__(self, other):
        return self.top_speed > other.top_speed


mustang = Car(make='Ford', model_name='Mustang', top_speed=120, color="Yellow")
mustang1 = Car(make='Ford', model_name='Mustang', top_speed=110, color="Yellow")
mustang.accererate()
print(mustang.current_speed)
print(mustang > mustang1)
mustang.accererate(50)
print(mustang.current_speed)

