# Korzystając z wikipedii utwórz klasy - Kot, Pies, Człowiek.
# Każda z nich powinna dziedziczyć z nadrzędnej klasy Ssaki.
# Klasa Ssaki powinna dziedziczyć z klasy Zwierzęta.
# Utwórz obiekty klas - kot, pies i człowiek, udowodnij, że rzeczywiście korzystają z klas rodziców.

class zwierzeta:
    def __init__(self):
        print('Zwierzęta oddychają i jedzą')


class ssaki(zwierzeta):
    def __init__(self):
        print('Ssaki są żyworodne')
        super().__init__()


class kot(ssaki):
    def __init__(self, name):
        print(name, "jest kotem")
        print('Koty miauczą')
        super().__init__()


class pies(ssaki):
    def __init__(self, name):
        print(name, "jest psem")
        print('Psy szczekają')
        super().__init__()


class czlowiek(ssaki):
    def __init__(self, name):
        print(name, "jest człowiekiem")
        print('Ludzie mówią')
        super().__init__()


tomek = czlowiek('Tomek')
print('*********')

burek = pies('Burek')
print('*********')

kicia = kot('Kicia')
print('*********')



