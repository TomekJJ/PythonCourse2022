def cut_cake():
    parts = int(input('podaj liczbę 1 o 10 ->'))
    return 10 / parts


def main():
    try:
        result = cut_cake()
    except (ZeroDivisionError, ValueError) as error:
        print('Błąd', error)
    else:
        print(result)
    finally:
        print('KONIEC PROGRAMU')

if __name__ == '__main__':
    main()

