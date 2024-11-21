class Animal:
    name = ""
    sound = ""

    def speak(self):
        return f"{self.name} says {self.sound}"


class Dog(Animal):
    name = "Dog"
    sound = "ruff, ruff!"


class Cat(Animal):
    name = "Cat"
    sound = "miaow!"


tom = Cat()
print(tom.speak())

spike = Dog()
print(spike.speak())

"""

 Polygon
    - number_of_sides
    - calculate_area

 Triangle,
 Square

"""


class Polygon:
    number_of_sides = 3

    def calculate_area(self):
        pass


class Triangle(Polygon):

    def __init__(self, width, height):
        super().__init__()
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height / 2


class Rectangle(Polygon):

    def __init__(self, width, height):
        super().__init__()
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height


class Square(Rectangle):

    number_of_sides = 4

    def __init__(self, side):
        super().__init__(side, side)
