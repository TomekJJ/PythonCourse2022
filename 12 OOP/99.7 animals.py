
from abc import ABC, abstractmethod # abstrakcję trzeba importować

class Animal(ABC):
    @abstractmethod
    def poop(self):
        pass

class Horse(Animal):

    def poop(self):
        print("Poop poop")

    def fly(self):
        print("Horse can't fly")


class Unicorn(Animal):

    def poop(self):
        print("Rainboooowww")

    def fly(self):
        print("Unicorn can fly with magical power")


class Cat(Animal):
    def meow(self):
        return "meow meow"

    def poop(self):
       print("Kuweta")

def family_test(animal): # animal może być dowowlnym obiektem dopóki ma metodę poop
    animal.poop()


arrow = Horse()
cute = Unicorn()
kity = Cat()

family_test(arrow)
family_test(cute)
family_test(kity)