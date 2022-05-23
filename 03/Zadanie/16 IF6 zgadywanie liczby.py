#Zapytaj użytkownika o numer od 1 do 100, jeśli użytkownik zgadnie liczbę ukrytą przez programistę wyświetl komunikat “gratulacje!”,
# w przeciwnym razie wyświetl “pudło!”.

x = 4
z = int(input('Podaj jakąś liczbę -->'))

if x == z:
    print("Gratulacje! Zgadłeś")
else:
    print('Pudło!')