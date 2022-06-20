def get_weather():
    # pobiera z api informacje o pogodzie
    # jesli dostaniemy bład --> zwróc własny błąd
    # return temperatura

    weather = input("podaj pogodę - > sun / rain ")

    if weather == 'sun':
        return 'słońce'
    elif weather == "rain":
        return 'chmurka'
    else:
        raise TypeError("niezana pogoda")

def main():
    print('jelo')

    try:
        current_weather = get_weather()
    except TypeError as err:
        print(err)
    else:
        print(current_weather)

if __name__ == '__main__':
    main()
