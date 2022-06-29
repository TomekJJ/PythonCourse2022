# Stwórz abstrakcyjną klasę Pojazdy. Utwórz potomne klasy pojazdy np. Samochód, Rower, Autobus, Ciężarówki.
# Dodaj opisy zgodne z tym jak te pojazdy są klasyfikowane.
# Jaki rodzaj dokumentu jest potrzebny, by kierować poszczegolnym pojazdem.

from abc import ABC, abstractmethod

class Pojazdy:
    @abstractmethod  # dekorator zawsze nad nazwą metody !!!
    def show_document(self):
        pass

    @abstractmethod # dekorator zawsze nad nazwą metody !!!
    def show_classifiation(self):
        pass

class Samochod(Pojazdy):
    def __init__(self,name):
        self.name = name

    def show_classifiation(self, name):
        print(f'Pojazd {name} jest samochodem')

    def show_document(self, name):
        print(f'Aby prowadzić {name} potrzebujesz prawa jazdy kat. B')


class Rower(Pojazdy):
    def __init__(self,name):
        self.name = name

    def show_classifiation(self, name):
        print(f'Pojazd {name} jest rowerem')

    def show_document(self, name):
        print(f'Aby prowadzić {name} potrzebujesz karty rowerowej')


class Autobus(Pojazdy):
    def __init__(self,name):
        self.name = name

    def show_classifiation(self, name):
        print(f'Pojazd {name} jest autobusem')

    def show_document(self, name):
        print(f'Aby prowadzić {name} potrzebujesz prawa jazdy kat. D')


class Ciezarowka(Pojazdy):
    def __init__(self,name):
        self.name = name

    def show_classifiation(self, name):
        print(f'Pojazd {name} jest ciężarówką')

    def show_document(self, name):
        print(f'Aby prowadzić {name} potrzebujesz prawa jazdy kat. C+E')

def main():
    fiat = Samochod('fiat 500')
    opel = Samochod('opel corsa')
    giant = Rower("rower giant")
    autosan = Autobus("Autosan")

    fiat.show_classifiation("fiat 500")
    fiat.show_document("fiat 500")
    opel.show_document("opel corsa")

    giant.show_document("rower giant")
    autosan.show_document('autosan')

if __name__ == '__main__':
    main()

