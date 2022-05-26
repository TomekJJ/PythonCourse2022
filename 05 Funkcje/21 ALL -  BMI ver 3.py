# Skorzystaj ze swojego kodu bmi.py.
# Rozbij liczenie bmi na funkcję obliczającą bmi na podstawie danych użytkownika oraz zwracającą odpowiednią wartość (niedowaga, waga normalna, nadwaga, otyłość) w zależności od otrzymanego parametru.

def calculate_bmi(weight, height):
    bmi_result = weight / (height / 100) ** 2
    bmi_result = round(bmi_result, 2)
    return bmi_result

def get_bmi_status(bmi):
    if bmi > 25:
        return("Masz nadwagę")
    elif bmi >=18.5:
        return("Twoja waga jest prawidłowa")
    elif bmi < 18.5:
        return("Masz niedowagę")
    else:
        return('błąd!')

def main():
    '''#1 pobranie danych użytkownika
    #2 wywołanie obliczeń
    #3 wyświetlenie statusu'''
    weight = float(input('Ile ważysz (w kg)? '))
    height = float(input('Jaki jest Twój wzrost? (w cm) '))


    result = calculate_bmi(weight, height)
    print(f'Twoje bmi to: {result}')

    check_result = get_bmi_status(result)
    print(check_result)

main()
