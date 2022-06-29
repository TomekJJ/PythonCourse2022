from abc import ABC, abstractmethod

class AbstractShape(ABC): #klasa abstrakcyjna
    @abstractmethod # dekorator, mówi, że każda metoda dziedzicząca musi mieć sides
    def sides(self):
        pass

class Triangle(AbstractShape):
    def sides(self):
        return 3

class Square(AbstractShape):
    def sides(self):
        return 4

    def area(self, side):
        return side * side

t = Triangle()
print(t.sides())

s = Square()
print(s.sides())
print(s.area(3))