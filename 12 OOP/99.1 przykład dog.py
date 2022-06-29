
class Canis:
    paws = 4

    def __init__(self):
        print('Canis is an animal')

    def show(self):
        print('🐶🐶🐶🐶🐶🐶🐶🐶🐶')

    def highligh(self):
        print('!!!!!!!!!!!!!!!!')

class Dog(Canis):   # dziedziczenie
    kingdom = 'animals'

    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    def bark(self, sound):
        print(sound * self.age)

    def show(self):
        super().show() ## skorzystaj z rodzica
        txt = f'My dog {self.name}, age: {self.age} is breed {self.breed}'
        print(txt)

class Fox(Canis):
    def __init__(self):
        print("create fox")

dyzio = Dog("Dyzio", 3, "mops")
dyzio.bark('hauu')
print(dyzio.paws)
print(dyzio.show())

print('************************')
wolfik =  Canis()
wolfik.show()

print('************************')
fox = Fox()
fox.show()

print('************************')
dyzio.highligh()
dyzio.show()