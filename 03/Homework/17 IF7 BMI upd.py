# Kalkulator BMI
# wyświetli w zależności od wyniku: niedowaga / waga normalna / nadwaga / otyłość.


w = int(input('Ile ważysz (w kg)? '))
h = int(input('Jaki jest Twój wzrost? (w cm) '))


bmi = w / (h/100) ** 2
bmi = round(bmi, 2)

print('Twoje BMI to:', bmi)

if bmi > 25:
    print("Masz nadwagę")
elif bmi >=18.5:
    print("Twoja waga jest prawidłowa")
elif bmi < 18.5:
    print("Masz niedowagę")
else:
    print('błąd!')

