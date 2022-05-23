# 1. Czy ciąg znaków składa się tylko z cyfr

txt = "12345646"
print(f'Ciąg {txt} zawiera same cyfry ->', txt.isdigit())
print(f'Ciąg {txt} zawiera same cyfry ->', txt.isnumeric())

# 2. Jak wyświelić wyśrodkowany tekst od zadanej szerokości i puste miejsca wypełnić gwiazdką?
txt2 = "tata"
print(f'wyśrodkoweny text ->', txt2.center(10, "*"))

# 3. Jaka metoda usunie znaki tylko z prawej strony?
txt3 = 'www.example.com'
print(txt3.lstrip('w.'))
print(txt3.removeprefix("www.",))

txt33 = "AAATTTGGCCAAAA"
print(txt33.rstrip('A'))

# 4. Jak sprawdzić czy ciąg ma co najmniej jedną dużą literę?
txt4 = "litwoojczyznomojA"
# print(txt4.isalnum())
# print(txt4.islower())
# print(txt4.isupper())

one_upper = txt4.isalpha() and (not txt4.islower() and not txt4.isupper())

print(one_upper)

# 5. Policz ile razy zadany ciąg znaków wystąpił w ciągu znaków?
txt5 = "bananana"
print(txt5.count("na"))
