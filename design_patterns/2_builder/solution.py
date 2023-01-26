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
        self.car = Car('', '', '', 0)

    def set_color(self, color: str):
        self.car.color = color
        return self

    def set_brand(self, brand: str):
        self.car.brand = brand
        return self

    def set_year(self, year: int):
        self.car.year = year
        return self

    def set_model(self, model: str):
        self.car.model = model
        return self

    def build(self):
        return self.car

builder = CarBuilder()
car = builder.set_color("White").set_year(2019).set_brand("Toyota").set_model("Yaris").build()
print(car)