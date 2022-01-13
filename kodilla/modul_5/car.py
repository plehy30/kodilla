class Car:
    def __init__(self, make, model_name, top_speed, color):
        self.make = make
        self.model_name = model_name
        self.top_speed = top_speed
        self.color = color

        self._current_speed = 0

    @property
    def current_speed(self):
        return self._current_speed

    @current_speed.setter
    def current_speed(self, value):
        if value <= self.top_speed:
            self._current_speed = value
        else:
            raise ValueError(f'Value {value} jest wieksze od {self.top_speed}')

    def accererate(self, step=10):
        self._current_speed += step

    def decelerate(self, step=10):
        self._current_speed -= step

    def __str__(self):
        return f'{self.color} {self.model_name} {self.make}'

    def __repr__(self):
        return f'Car(make={self.make} model={self.model_name} top_speed={self.top_speed} color={self.color}'

    def __gt__(self, other):
        return self.top_speed > other.top_speed


mustang = Car(make='Ford', model_name='Mustang', top_speed=120, color="Yellow")
mustang1 = Car(make='Ford', model_name='Mustang', top_speed=110, color="Yellow")
mustang.current_speed = 30
mustang.accererate()
print(mustang.current_speed)
print(mustang > mustang1)
mustang.accererate(60)
print(mustang.current_speed)
