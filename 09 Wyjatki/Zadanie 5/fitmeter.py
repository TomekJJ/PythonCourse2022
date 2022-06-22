# 1▹ Stwórz moduł, który będzie przechowywał funkcję obliczającą bmi.py. Zaimportuj module do pliku fitmeter.py. Nowy plik będzie informował użytkownika o jego aktualnym BMI i na podstawie wyniku (niedowaga, nadwaga, otyłość) sugerował zmiany w stylu życia pobierane z odpowiedniego pliku.
    # Utwórz plik bmi.py zawierający metodę obliczania bmi. Metoda zwraca wartości: niedowaga, waga normalna, nadwaga, otyłość.
    # Utwórz 4 pliki .txt zawierające porady.
    # Utwórz plik fitmeter.py, który zaimportuje moduł bmi.
    # fitmeter.py pobierze wagę i wzrost pacjenta i przekaże do odpowiedniej funkcji z modułu bmi.
    # Na podstawie zwróconej wartości fitmeter.py wyświetli odpowiednie porady dla pacjenta.


from bmi import *


def give_advice(bmi_value):
    if bmi_value > 25:
        with open('Porada1.txt') as f:
            content = f.read()
            print(content)
    elif bmi_value >=18.5:
        with open('Porada2.txt') as f:
            content = f.read()
            print(content)
    elif bmi_value < 18.5:
        with open('Porada3.txt') as f:
            content = f.read()
            print(content)
    else:
        return ('błąd!')

def get_value(massage, min_max):
    while True:
        try:
            value = float(input(massage))
            minimum, maximum = min_max # rozpaowanie krotki
            if not value in range(minimum, maximum+1):
                raise ValueError

        except (TypeError, ValueError):
            print('Wartość jest nieprawidłowa, spróbuj jeszcze raz...')
        else:
            return value

def main():
    weight = get_value('Ile ważysz (w kg)?', (20, 200))
    height = get_value('Jaki jest Twój wzrost? (w cm)', (140, 220))

    bmi = calculate_bmi(weight,height)
    print(f'Twoje bmi to: {bmi}')
    print(get_bmi_status(bmi))
    give_advice(bmi)

main()