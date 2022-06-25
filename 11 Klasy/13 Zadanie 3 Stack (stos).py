# LIFO
# show - wyświetl cały stos
# push - dodaj element do stosu
# get element - wyciągnij element ze stosul


class Stack:
    def __init__(self, lifo):
        self.lifo = lifo

    def show(self):
        print('aktualny stos', self.lifo)


    def put_element(self, item):
        self.lifo.append(item)


    def get_element(self):
        return self.lifo.pop(-1)


def main():
    # wyświetlanie
    q = Stack(['Ola', 'Tomek', 'Ania', 'Henio'])
    q.show()

    # dodawanie elementu
    q.put_element("Rita")
    q.show()

    # zabieranie elementu
    x = q.get_element()
    print('Wyjęto:', x)
    q.show()

    # zabieranie elementu (2)
    x = q.get_element()
    print('Wyjęto:', x)
    q.show()

if __name__ == '__main__':
    main()