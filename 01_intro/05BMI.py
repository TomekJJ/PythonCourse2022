# Kalkulator BMI
w = input('Ile ważysz (w kg)? ')
h = input('Jaki jest Twój wzrost? (w cm) ')

#zmiana na liczby całkowite lub dziesiętne
w = int(w)
h = float(h)

#alternatywnie można od razu w funkcji input
#w = float(input('Ile ważysz (w kg)?'))

bmi = w / (h/100) ** 2
bmi = round(bmi, 2)

print('Twoje BMI to:', bmi)
