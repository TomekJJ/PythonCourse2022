# Napisz prostą grę, w której użytkownik musi zgadnąć liczbę od 0 - 20 ukrytą w programie (np. secret_num = 5).
# Pytaj użytkownika o podanie liczby tak długo, aż nie zgadnie.

sec_num = 5
user_num = int(input("podaj liczbę"))

while(user_num != sec_num):
    print("spróbuj jeszcze raz")
    user_num = int(input("podaj liczbę"))

print(f'brawo' ,sec_num, "to szukana liczba!")