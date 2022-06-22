# kalkulacja kosztów wyprawy

dystans = input('podaj dystans (w km)? ')
dystans = int(dystans)
# int można też od razu z inputem

spalanie = input('podaj spalanie (l/100km)')
spalanie = int(spalanie)
cena = input('podaj cenę benzyny (zł)')
cena = int(cena)

koszt_wyprawy = dystans/100 * spalanie * cena
print(koszt_wyprawy)
