# do zrobienie w domu (github)

#  W nowym pliku utwórz skrypt, który na podstawie podanych składowych kształtów pomieszczeń oraz ich wymiarów zwraca powierzchnię budynku.


from polafigur import *

def main():
    rooms = {
        "kwadrat": [4, 5, 2],
        "prostokąt": [[3, 4], [5, 3]],
        "trójkąt": [[2, 3], [4, 2]]
    }
    total = 0

    for shape, rooms in rooms.items():
        if shape == "kwadrat":
            for room in rooms:
                total += oblicz_kwadrat(room)
        if shape == "prostokąt":
            for room in rooms:
                a, b = room
                total += oblicz_prostokat(a, b)
        if shape == "trójkąt":
            for room in rooms:
                a, h = room
                total += oblicz_trojkat(a, h)

    print(f'Całkowita powierzchnia to {total} m2')

if __name__ == '__main__':
    main()


