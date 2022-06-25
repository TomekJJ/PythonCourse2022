# student_anna = {
#   'name': 'Anna',
#   'lastname': 'Kowalska',
#   'age': '23',
#   'subject': 'Computing Science',
#   'email': 'anna.kowalska@university.com'
# }
#
# student_piotr = {
#   'name': 'Piotr',
#   'lastname': 'Nowak',
#   'age': '22',
#   'subject': 'Computing Science',
#   'email': 'piotr.nowak@university.com'
# }

class Student:
    university_code = 'UEK'

    def __init__(self, imie, nazwisko, wiek):
       self.first = imie
       self.last = nazwisko
       self.age = wiek

    def email(self):
      return f'{self.first}.{self.last}@{self.university_code}.com'.lower()

    def hello(self):
        print('HELOŁ')

anna = Student('Anna', "Kowalska", 23)
piotr = Student('Piotr', "Nowak", 22)

print(anna.last, anna.first, anna.age, anna.email())
print(piotr.last, piotr.first, piotr.age, piotr.email())

print(anna.__dict__) # jakie pola należą do obiektu 'anna"
print(Student.__dict__) # jakie pola nalezą do klasy student

# anna wzięła ślub :)
print('....................')
anna.last = "Smith"
print(anna.last, anna.first, anna.email())

# wywoływanie metody na dwa sposoby
print('....................')
anna.hello()
Student.hello(anna)

print(Student.email(anna))

