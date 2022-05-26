magic = 'abrakadabra'

# funkcja na stringu
print(len(magic))


# metoda an stringu
print(magic.upper())

def mood():
    print("How are you")
mood()

for _ in range (3):
    mood()

print(".........")

def my_mood(answear):
    print('My mood today:')
    print(answear)

resp = input("how are you?")
my_mood(resp)
my_mood('Good')

a = "Świetnie"
my_mood(a)

def my_mood2(answear):
    return answear * 2

print(my_mood2("lala"))

