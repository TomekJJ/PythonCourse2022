# Napisać funkcję, która oblicza pole koła na podstawie zadanego promienia.

def liczenie_pola_kola():
    promien = float(input('Podaj promień: '))
    pole = 3.1415 * promien ** 2
    print(f'pole koła o promieniu {promien} to {pole}')

liczenie_pola_kola()

# ---------
# inaczej
def calc_circle_field(r):
    pi = 3.14
    return pi * r**2

radius = float(input('podaj promień -->'))
field = calc_circle_field(radius)
print('pole koła to:', field)






