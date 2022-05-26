# Napisz grę ciepło - zimno tak, aby korzystać z funkcji.

def sprawdz_liczbe(user, komp):
    if user == komp:
        print("wygrałeś")
    elif komp >= user:
        print('za mała liczba, spróbuj jeszcze raz')
    elif user >= komp:
       print('za duża liczba, spróbuj jeszcze raz')


komp = 10
user = int(input('podaj liczbę:'))
while(user == komp):
        sprawdz_liczbe(user,komp)


