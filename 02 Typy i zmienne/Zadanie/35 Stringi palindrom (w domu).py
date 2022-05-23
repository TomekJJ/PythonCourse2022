'''Palindrom to wyrażenie brzmiące tak samo czytane od lewej do prawej i od prawej do lewej np.: Kobyła ma mały bok.
Pozwól użytkownikowi wprowadzić dowolne zdanie.
Następnie sprawdź czy wprowadzone wyrażenie jest palindromem.
'''

zdanie = input("wprowadz zdanie: ")

half = len(zdanie)/2
half = int(half)

first_half = zdanie[0:half]
second_half = zdanie[half:]
second_half_rev = second_half[::-1]


print(f'Czy podane zdanie jest palindromem? ', first_half == second_half_rev)
