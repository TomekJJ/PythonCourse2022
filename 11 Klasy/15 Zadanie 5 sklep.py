class Sklep:
    def __init__(self, produkty):
        self.produkty = produkty

    def show(self):
        print('Aktualny asortyment sklepu: ', self.produkty)


    def try_item(self, item):
        if item in self.produkty:
            print(f'przymierzasz {item}')
        else:
            print("nie ma takiego produktu")


    def buy_item(self,item):
        if item in self.produkty:
            self.produkty.remove(item)
        else:
            print("nie ma takiego produktu")

    def return_item(self, item):
            self.produkty.append(item)

def main():
    # wyświetlanie asortymentu
    asortyment = Sklep(['Buty', 'Kurtka', 'Koszulka', 'Spodnie', 'Pasek', 'Skarpetki'])
    asortyment.show()

    # przymierzanie
    x = str(input("co chcesz przymierzyć? "))
    asortyment.try_item(x)

    # kupowanie
    x = str(input("co chcesz kupić "))
    asortyment.buy_item(x)
    asortyment.show()

    # zwracanie
    x = str(input("co chcesz zwrócić "))
    asortyment.return_item(x)
    asortyment.show()


if __name__ == '__main__':
    main()