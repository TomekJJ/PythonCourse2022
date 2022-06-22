LISTA = [1, 2, 3, 5, 10, 11, 12, 15, 16, 20]


def give_even(lista):
    lista_parzyste = []
    for num in lista:
        if num % 2 == 0:
            lista_parzyste.append(num)
    return lista_parzyste


def main():
     print('Liczby parzyste to', give_even(LISTA))


main()
