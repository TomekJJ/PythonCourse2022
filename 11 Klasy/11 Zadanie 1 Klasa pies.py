class Pies:
    def __init__(self, imie, kolor, rasa):
        self.imie = imie
        self.kolor = kolor
        self.rasa = rasa

    def szczekaj(self):
        print(f'{self.imie} robi HAŁ HAŁ HAŁ')

    def machaj_ogonem(self):
        print(f'{self.kolor} {self.rasa} {self.imie} macha ogonem')

def main():
    burek = Pies('Burek', 'brązowy', 'kundel')
    azor = Pies('Azor', 'szary', 'wilczur')
    tola = Pies('Tola', 'biały', 'labrador')
    nela = Pies('Nela', 'biało-czarny', 'dalmatyńczyk')

    tola.machaj_ogonem()
    tola.machaj_ogonem()
    Pies.szczekaj(tola)

    Pies.machaj_ogonem(nela)

if __name__ == '__main__'
    main()