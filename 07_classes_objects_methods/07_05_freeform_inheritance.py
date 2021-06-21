'''
Build on your previous freeform exercise.

Create subclasses of two of the existing classes. Create a subclass of
one of those so that the hierarchy is at least three levels.

Build these classes out like we did in the previous exercises.

If you cannot think of a way to build on your freeform exercise,
you can start from scratch here.

We encourage you to be creative and try to think of an example of
your own for this exercise but if you are stuck, some ideas include:

- A Vehicle superclass, with Truck and Motorcycle subclasses.
- A Restaurant superclass, with Gourmet and FastFood subclasses.

'''
class Vehicle():

    def __init__(self, brand, color, wheels, fuel, max_speed):
        self.brand = brand
        self.color = color
        self.wheels = wheels
        self.fuel = fuel
        self.max_speed = max_speed



class Car(Vehicle):
    def __init__(self, brand, color, wheels, fuel, max_speed, doors, style, amount_seats):
        super().__init__(brand, color, wheels, fuel, max_speed)
        self.doors = doors
        self.style = style
        self.amount_seats = amount_seats

    def __str__(self):
        return f"The car is a {self.style}, {self.brand}, it's {self.color}, have {self.wheels} wheels, runs with {self.fuel}," \
               f"it's max speed is {self.max_speed}, it has {self.doors} it possess {self.amount_seats}"




class Truck(Vehicle):
    def __init__(self, brand, color, wheels, fuel, max_speed, transmition):
        super().__init__(brand, color, wheels, fuel, max_speed)
        self.transmition = transmition

    def __str__(self):
        return f"This is a Truck from {self.brand}, color {self.color}, it has {self.wheels} wheels" \
               f"runs with {self.fuel}, it has a max speed of {self.max_speed} and possess {self.transmition} transmitions"


class Motocicle(Vehicle):
    def __init__(self, brand, color, wheels, fuel, max_speed, style, sound):
        super().__init__(brand, color, wheels, fuel, max_speed)
        self.style = style
        self.sound = sound

    def __str__(self):
        return f"This is {self.color} {self.brand} motocicle, it has {self.wheels} wheels" \
               f"it runs with {self.fuel}, it can go at max spped of {self.max_speed}k/h and it sounds like a {self.sound}"



class Bicicle(Vehicle):
    def __init__(self, brand, color, wheels, style, max_speed, num_gear):
        super().__init__(brand, color, wheels, style, max_speed)
        self.num_gear = num_gear

    def __str__(self):
        return f"This is a bike brand {self.brand}, color {self.color}, it has only {self.wheels} wheels" \
               f"ti can goes as faster as {self.max_speed}km/h, it possess {self.num_gear} gears"



class Scooter(Vehicle):

    def __str__(self,):
        return f"The brand of the Scooter is {self.brand}, it's {self.color}, it only has {self.wheels} wheels, work with {self.fuel} and it's maximum speed is {self.max_speed}k/h"

mazda = Car("Mazda", "white", 4, "regular", 250, 4, "sedan", 4)
deer = Truck("Deer", "brown", 4, "diesel", 120, 8)
yamaha = Motocicle("Yamaha", "blue", 2, "regular", 170, "racer cafe", "tiger")
scooter = Scooter("china", "red", 2, "battery", 30)
trek = Bicicle("Trek", "white", 2, "downhill", 60, 15)



print(mazda)
print(deer)
print(yamaha)
print(trek)
print(scooter)