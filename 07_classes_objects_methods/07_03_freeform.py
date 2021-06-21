'''
#- Write a script with three classes that model everyday objects.
#- Each class should have an __init__ method that sets attributes
    to a default value if values are not passed.
#- Create at least two objects of each class using the __init__ method.
#- Each object should have at least three attributes.
#- Each class should have at least two class attributes.
#- Create a print method in each class that prints out the attributes
    in a nicely formatted string.
#- Include a __str__ method in each class.
- Overload the __add__ method in one of the classes so that it's possible
    to add attributes of two instances of that class using the + operator.
- Once the objects are created, change some of the attribute values.

Be creative. Have some fun. :)
Using objects you can model anything you want.
Cars, animals, poker games, sports teams, trees, beers, people etc...


'''
class Beer():

    def __init__(self, type, taste, alcohol):
        self.type = type
        self.taste = taste
        self.alcohol = alcohol

    def __str__(self):
        return f"the beer is type is {self.type}, it has a {self.taste} beer and it has {self.alcohol}% of alcohol."


class People():

    def __init__(self, name, size, color, hair):
        self.name = name
        self.size = size
        self.color = color
        self.hair = hair

    def __str__(self):
        return f"This is {self.name}. {self.name} is {self.size} person, the skin color of {self.name} is {self.color}."

class Animals():

    def __init__(self, name, skin, size):
        self.name = name
        self.skin = skin
        self.size = size

    def __str__(self):
        return f"{self.name}s are {self.size} animals. They have {self.skin}."

#beer objects
lager = Beer("Lager", "middel", 5)
pilsen = Beer("Pilsen", "light", 7)
agustina = Beer("Agustina", "dark", 12)
print(agustina)

#people
jorge = People("Jorge", "tall", "white", "brown and short")
Karla = People("Karla", "small", "brown", "blond a long")
Ina = People("Ina", "medium", "black", "curly and long")
print(jorge)

#animals
dog = Animals("dog", "fur", "small")
lion = Animals("cat", "fur", "big")
dolfin = Animals("dolfin", "not fur", "big")
print(dog)