sum_grades = 0
for i in range(3):
   subject = input("podaj nazwę przedmiotu: ")
   grade = int(input(f'podaj ocenę z {subject}: '))
   print(f'ocena z {subject}: to {grade}')
   sum_grades += grade

print(f'Twoja średnia z 3 przedmiotów to {sum_grades/3}')