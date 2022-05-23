# Stwórz zmienną password.
# Hasło powinno składać z liter i cyfr, zwierać conajmniej 1 dużą literę i mieć długość conajmniej 8 znaków.
# Poinformuj użytkownika, jeśli wpisane hasło jest nie poprawne.
# Wyświetl różne komunikaty w zależności od rodzaju błędu.

passw = input("wprowadź hasło -> ")

check1 = 0
check2 = 0
check3 = 0

if passw.isalnum() and not passw.isdigit() and not passw.isalpha():
#   print("Hasło zawiera litery oraz cyfry")
    check1 = 1
else:
  print ("Błąd. Hasło nie składa się z liter i cyfr")

if passw.isalnum() and not passw.islower() and not passw.isupper():
#    print("Hasło zawieraco najmniej jedną dużą i jedną małą literę")
    check2 = 1
else:
    print("Błąd. Hasło nie zawiera co najmniej jednej dużej i jednej małej litery")


if len(passw) >= 8:
#    print('Hasło zawiera co najmniej 8 znaków')
    check3 = 1
else:
    print("Błąd. Hasło nie zawiera co najmniej 8 znaków")

checksum = check1 +  check2 + check3
if checksum == 3:
    print("Hasło jest poprawne!")
else:
    print("podaj hasło jeszcze raz")
