class Car:
    def __init__(self, name, color, speed, is_police=False):
        self.name = name
        self.color = color
        self.is_police = is_police
        self.speed = speed

    def go(self):
        print(f'{self.color} {self.name} поехала')

    def stop(self):
        print(f'{self.color} {self.name} поехала')

    def turn(self, direction):
        self.direction = direction
        print(f'{self.color} {self.name} сделала поворот {self.direction}')

    def show_speed(self):
        print(f'скорость автомобиля: {self.speed}')

class TownCar(Car):
    def __init__(self, name, color, speed):
        super().__init__(name, color, speed)

    def show_speed(self):
        print(f'Скорость: {self.speed}') if self.speed <= int(60) else print('Превышена максимальная скорость')

class SportCar(Car):
    pass

class WorkCar(Car):
    def __init__(self, name, color, speed):
        super().__init__(name, color, speed)

    def show_speed(self):
        print(f'Скорость: {self.speed}') if self.speed <= int(40) else print('Превышена максимальная скорость')

class PoliceCar(Car):
    def __init__(self, name, color, speed):
        super().__init__(name, color, speed, True)

c = Car(40, 'white', 'bmw')
t = TownCar('ford', 'black', 70)
s = SportCar(40, 'orange', 'Lamborgini')
w = WorkCar(40, 'grey', 'shevrolet')
p = PoliceCar(40, 'red', 'ferrari')

t.go()
t.turn('налево')
t.stop()
t.show_speed() # странно. при выполении команды постоянно показывает информацию black Ford