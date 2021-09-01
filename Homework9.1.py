class Road:
    __length = None
    __width = None
    weight = None
    thickness = None

    def __init__(self, length, width):
        self.length = length
        self.width = width
        print('Создали объект m')

    def mass_calculation(self, length, width, weight, thickness):
        mass_calculation = length * width * weight * thickness / 10
        print(f'Потребуется {round(mass_calculation)}т для покрытия всей дороги')

m = Road(5000, 20)
m.mass_calculation(5000, 20, 25, 0.05)