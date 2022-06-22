# 5 użytkowników poproś o podanie 4 przedmiotów szkolnych,
# Sprawdź czy przedmioty powtarzają się na listach.
# Wyświetl najpopularniejszy przedmiot.
# Uwzględnij fakt, że użytkownicy mogą zapisać przedmioty małymi, drukowanymi lub zaczynając od dużej litery

# user1 = input('1. Podaj 4 przedmioty szkolne -> ').lower()
# user2 = input('2. Podaj 4 przedmioty szkolne -> ').lower()
# user3 = input('3. Podaj 4 przedmioty szkolne -> ').lower()
# user4 = input('4. Podaj 4 przedmioty szkolne -> ').lower()

user1 = ['kredka', 'ołówek', 'plecak', 'zeszyt']
user2 = ['kredka', 'i', 'j', 'k']
user3 = ['a', 'i', 'ołówek', 'd']
user4 = ['i', 'i', 'g', 'ołówek']

lista_glob = user1 + user2 + user3 + user4

przedmioty_counter = {}

for przedmiot in lista_glob:
    if przedmiot in przedmioty_counter:
        przedmioty_counter[przedmiot] += 1
    else:
        przedmioty_counter[przedmiot] = 1

for key, value in przedmioty_counter.items():
    if value > 1:
        print(f'Przedmiot {key} potwarza się {value} razy')



print(f'Najczęściej powtarzającym się przedmiotem jest xxx  powtarza się {max(przedmioty_counter.values())} razy')
