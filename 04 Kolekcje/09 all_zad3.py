# Utwórz dowolną tablicę n x n zawierającą dowolny znak, a następnie wyświetl jej elementy w formie tabeli n x n.
# Elementy powinny być oddzielone spacją
n = int(input('podaj liczbę'))
tab = [['-'] * n] * n

print(tab)
print('........')

for row in tab:
    for i in row:
        print(i, end=" ")
    print() # drukuje entera

