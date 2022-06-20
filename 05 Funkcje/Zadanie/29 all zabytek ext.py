CAR = {
    'marka' : 'Opel',
    'model' : 'Corsa',
    'rocznik' : 1999,
    'czy_oryginalny': True
    }

def show_dict(CAR):
    print(CAR)

def is_25yo(CAR):
    if CAR['rocznik'] <= 1997:
        print(f"Twój samochód {CAR['marka']} {CAR['model']} ma więcej niż 25 lat")
        return True
    else:
        print(f"Twój samochód {CAR['marka']} {CAR['model']} ma mniej niż 25 lat")
        return False

def is_original(CAR):
    if CAR['czy_oryginalny'] == True:
        print(f"Twój samochód {CAR['marka']} {CAR['model']} ma co najmniej 75% oryginalnych części")
        return True
    else:
        print(f"Twój samochód {CAR['marka']} {CAR['model']} nie ma co najmniej 75% oryginalnych części")
        return False

def main():
    show_dict(CAR)
    wiek = is_25yo(CAR)
    czesci = is_original(CAR)

    print('************************')
    if wiek and czesci == True:
        print(f"Gratulacje! Twój samochód {CAR['marka']} {CAR['model']} może być zarejestrowany jako zabytek")
    else:
        print(f"Twój samochód {CAR['marka']} {CAR['model']} nie może być zarejestrowany jako zabytek")

main()