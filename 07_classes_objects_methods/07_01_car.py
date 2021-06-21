'''
Write a class to model a car. The class should:

1. Set the attributes model, year, and max_speed in the __init__() method.
2. Have a method that increases the max_speed of the car by 5 when called.
3. Have a method that prints the details of the car.

Create at least two different objects of this Car class and demonstrate
changing the objects attributes.

'''

class Car:

    def __init__(self, model, year, max_speed=0):
        self.model = model
        self.year = year
        self.max_speed = max_speed

    def accelerate(self):
        self.max_speed +=5
        return print(self.max_speed)

my_car = Car("Mazda", 1995, 5)
print(my_car.max_speed)
