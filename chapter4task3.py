class Car:
    def __init__(self, mark, model, year):
        self.mark = mark
        self.model = model
        self.year = year
        self.odometr = 0
        self.fuel = 70

    def __add_distance(self, km):
        self.odometr += km

    def __subtract_fuel(self, km):
        self.fuel -= 10/km

    def drive(self, km):
        if (self.fuel - km/10) >= 0:
            self.__add_distance(km)
            self.__subtract_fuel(km)
            print("Lets Drive!!!")
        else:
            print("Need more Fuel, Fill up")

mashina = Car("Toyota", "Camry", "2014")
print(mashina.mark, mashina.model, mashina.year)
mashina.drive(100)
print(mashina.odometr)
print(mashina.fuel)


