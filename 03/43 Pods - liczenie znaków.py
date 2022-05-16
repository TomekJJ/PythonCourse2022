# W podanym przez użytkownika ciągu wejściowym policz wszystkie małe litery, wielkie litery, cyfry i znaki specjalne.

txt = input('Podaj ciąg znaków ->')
#txt = "aBrakadaBa123!"


lower_count = 0
upper_count = 0
digit_count = 0
special_count = 0

for i in txt:
    if i.islower():
        lower_count = lower_count + 1
        continue
    if i.isupper():
        upper_count = upper_count + 1
        continue
    if i.isdigit():
        digit_count = digit_count + 1
        continue
    if not i.isalpha():
        special_count = special_count + 1


print("Liczba małych liter: ", lower_count)
print("Liczba dużych liter: ", upper_count)
print("Liczba cyfr: =", digit_count)
print("Liczba znaków specjalnych: =", special_count)