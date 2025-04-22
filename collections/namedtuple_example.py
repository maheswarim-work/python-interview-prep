from collections import namedtuple

Car = namedtuple("Car", ["make", "model", "year"])

car = Car("BMW", "X3", "2020")
print(car)
print(car.make)
print(car.model)
print(car.year)

car = Car(make="Benz", model="GLC", year="2020")
print(car)
print(car.make)
print(car.model)
print(car.year)

print(isinstance(car, tuple))
