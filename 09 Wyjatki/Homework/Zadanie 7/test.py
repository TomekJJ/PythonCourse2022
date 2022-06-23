import os

while True:
    try:
        filename = input("podaj nazwę pliku (bez rozszerzenia): ") + ".txt"
        if not os.path.exists(filename):
            raise FileNotFoundError

    except (FileNotFoundError):
        print("Nie ma takiego pliku")
    else:
        print("JEST")
        break