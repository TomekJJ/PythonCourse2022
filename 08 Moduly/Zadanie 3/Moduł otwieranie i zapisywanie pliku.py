# Stwórz moduł, który zajmuje się jedynie otwieraniem plików - oferuje bezpieczny sposób odczytu oraz bezpieczny zapis.
# Funkcja czytająca pliki sprawdza najpierw czy dany plik istnieje oraz czy jest niepusty.
# Funkcja zapisująca do pliku chroni przed nadpisaniem istniejącego pliku.


import os

def open_file(filename):
    if not os.path.exists(filename):
        print('Nie ma takiego pliku')
    elif os.stat(filename).st_size == 0:
        print("Wskazny plik jest pusty")
    else:
        with open(filename, 'r') as f:
            file = f.read()

        return file


def write_file(filename, content):
    if os.path.exists(filename) and os.stat(filename).st_size > 0:
        print("Plik istnieje i nie jest pusty")
    else:
        with open(filename, 'w') as f:
            f.write(content)
    print(f'file {filename} is saved!')

def main():
    filename = "tekst.txt"
    filename2 = "testowy.txt"
    content = "to jest przykładowy tekst"

    write_file(filename2, content)

    result = open_file(filename2)
    print(result)

main()