# Znajdź największa wspólny dzielnik (NWD) dwóch liczby. Wykorzystaj algorytm Euklidesa.

def find_nwd(a, b):

    while True:
        reszta = a % b

        if reszta == 0:
            nwd = b
            return nwd
        else:
            a = b
            b = reszta


a = int(input("a -> "))
b = int(input('b -> '))

nwd = find_nwd(a, b)
print(f'największy wspólny dzielnik {a} i {b} to {nwd}')
