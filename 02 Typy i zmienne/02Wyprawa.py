# kalkulacja kosztów wyprawy

dystans = input('podaj dystans (w km)? ')
dystans = int(dystans)
spalanie = input('podaj spalanie (l/100km)')
spalanie = int(spalanie)
cena = input('podaj cenę benzyny (zł)')
cena = int(cena)

koszt_wyprawy = dystans/100 * spalanie * cena
print(koszt_wyprawy)
