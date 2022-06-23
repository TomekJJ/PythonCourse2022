# Wywołaj błąd związany z otwarciem pliku.
# Obsłuż w dowolny sposób każdy z powyższych błędów.

# Spróbuj odczytać plik, który nie istnieje.
import io

filename = "xxraport_bledow.txt"
filename2 = "raport_bledow.txt"

try:
    with open(filename, 'r') as f:
        content = f.read()
    print(content)
except FileNotFoundError:
    print("BLAD. Nie ma takiego pliku")

# Spróbuj odczytać wartość z pliku otwartym w trybie "w"
try:
    with open(filename2, 'w') as f:
        content = f.read()
    print(content)
except io.UnsupportedOperation:
    print("BŁAD. Nie da się odczytać pliku otwartego w trybie do zapisu")


# Spróbuj utworzyć plik, który już istnieje w trybie "x"
try:
    with open(filename2, 'x') as f:
        f.write('\n')
        f.write('Nowa linijka do zapisania')
except FileExistsError:
        print("BŁAD. Wskazany plik już istnieje!")