# napisz funkcję, która pyta użytkownika o pary książka + ocena i zapisuje je w programie

 # na liście
def add_book(books):
        title = input('podaj książkę: ')
        grade = input(f'Oceń książkę {title}: ')
        books.append((title,grade))

books = []
num = int(input('ile książek chcesz dodać? '))
for _ in range (num):
        add_book(books)

print(books)

# napisz funkcję, która zapyta o numer książki i wyświetli tytuł wraz z oceną
# obsłuż błąd użytkowniak (nieistniejący numer)

def get_book(books):
        counter = len(books)
        while True:
                index = int(input('podaj numer książki -> '))
                if index > counter:
                        print("nie ma takiej książki")
                else:
                        break
        index = index - 1 # index -= index
        print(books[index])

get_book(books)

# ze słownikiem
# def add_book2(books_dict)
#         title = input('podaj książkę: ')
#         grade = input(f'Oceń książkę {title}: ')
#         book_dict[title] = grade
#
# my_books = {
#        "LOTR": 9
# }
# add_book2(my_books)
# print(my_books)
#
# books_list = []
# for k, v in my.books.items()
#       books.list.append([k, v])
# print(books_list)
