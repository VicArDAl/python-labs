'''
Create two classes that model a rectangle and a circle. The rectangle class should
be constructed by length and width while the circle class should be constructed by
radius.

Write methods in the appropriate class so that you can calculate the area (of the rectangle and circle),
perimeter (of the rectangle) and circumference of the circle.

'''

class Rectangul():

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def __str__(self):
        return f"The area of the rectangle is {self.length * self.width} and it's perimeter is {2*self.length + 2*self.width}"

class Circle():

    def __init__(self, radius):
        self.radius = radius

    def __str__(self):
        return f"the area of the circle is {self.radius * self.radius * 3.14} and its circumference is {(self.radius + self.radius) * 3.14}"



rectangul = Rectangul(2, 2)
print(rectangul)


print(Circle(20))