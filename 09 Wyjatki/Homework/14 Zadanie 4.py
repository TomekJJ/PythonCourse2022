# Oblicz średnią arymetyczną z kilku liczb.
# Liczby będą podane przez użytkownika po przecinku.
# Napisz funkcję, która przyjmie wartości i wyświetli średnią.
# Program powinen być odporny na błędy użytkownika.
# Błędów nie wyświetlaj, ale rodzaj błędu zapisz do pliku.

def get_numbers():
    user_liczby = input("podaj liczby po przecinku: ")
    user_liczby = user_liczby.split(",")

    return user_liczby


def calculate_average(liczby):
    suma = 0
    for v in liczby:
        suma += float(v)
    srednia = suma / len(liczby)

    return srednia


def save_to_file(blad):
    with open('raport_bledow.txt', 'a', encoding='utf-8') as f:
        f.write('\n')
        f.write(blad)


def main():
    blad = ""
    liczby = get_numbers()
    print(f'podane wartości to {liczby}')

    try:
        srednia = calculate_average(liczby)
        print(f'Obliczona srednia to {srednia}')
    except ValueError as e:
        print("Z tych wartości nie da się obliczyć średniej")
        blad = "ValueErorr " + str(e)

    if blad != "":
        save_to_file(blad)
        # print(f'Błąd:  {blad}')





main()
