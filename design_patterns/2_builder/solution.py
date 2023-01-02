class Car:
    def __init__(self, color: str, brand: int, model: str, year: int):
        self.color = color
        self.brand = brand
        self.model = model
        self.year = year

    def __str__(self):
        return f'Car: {self.year} {self.color} {self.brand} {self.model}'

class CarBuilder:
    def __init__(self):
        self.computer = Car('', '', '', 0)

    def set_color(self, color: str):
        self.computer.color = color
        return self

    def set_brand(self, brand: str):
        self.computer.brand = brand
        return self

    def set_year(self, year: int):
        self.computer.year = year
        return self

    def set_model(self, model: str):
        self.computer.model = model
        return self

    def build(self):
        return self.computer

builder = CarBuilder()
car = builder.set_color("White").set_year(2019).set_brand("Toyota").set_model("Yaris").build()
print(car)