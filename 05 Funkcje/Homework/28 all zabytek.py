CAR = {
    'marka' : 'Opel',
    'model' : 'Corsa',
    'rocznik' : 1997
}

def show_dict(CAR):
    print(CAR)

def is_25yo(CAR):
    if CAR['rocznik'] <= 1997:
       print(f"Gratulacje! Twój samochód {CAR['marka']} {CAR['model']} może być zarejestrowany jako zabytek zabytek")
    else:
       print(f"Twój samochód {CAR['marka']} {CAR['model']} nie może być zarejestrowany jako zabytek")


def main():
    show_dict(CAR)
    is_25yo(CAR)

main()