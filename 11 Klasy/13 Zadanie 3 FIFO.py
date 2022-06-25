# Stwórz własną implementację kolejki FIFO.
# Klasa kolejka (Queue) powinna na starcie przyjmować listę elementów.
# Wśród metod powinny się znaleźć takie jak: wyswietlenie kolejki, sprawdzenie czy jest pusta, dodanie elementu do kolejki (put), wyjęcie elementu z kolejki (get).

class Queue:
    def __init__(self, fifo = []):
        self.fifo = fifo


    def show(self):
        print('aktualna kolejka', self.fifo)


    def is_empty(self):
        return len(self.fifo) == 0


    def put_element(self, item):
        self.fifo.append(item)


    def get_element(self):
        return self.fifo.pop(0)


def main():
    # wyświetlanie
    q = Queue(['Ola', 'Tomek', 'Ania', 'Henio'])
    q.show()

    # sprawdzanie czy pusta
    print(q.is_empty())

    # dodawanie elementu
    q.put_element("Rita")
    q.show()

    # zabieranie elementu
    x = q.get_element()
    print('Wyjęto:', x)
    q.show()


if __name__ == '__main__':
    main()