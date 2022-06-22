# Utwórz zmienną przechowującą dowolny ciąg znaków.
# Sprawdź czy utworzony string jest dłuższy niż 5 znaków oraz czy zawiera literę a.
# Jeśli zawiera, wszystkie litery a podmień na z i wyświetl powstały napis

txt = input("podaj ciąg znaków ->")

if len(txt) > 5 and 'a' in txt:
    print ("tekst zawiera więcej niż 5 znaków i zawiera literę a")
    print(txt.replace('a','z'))
else:
    print("Nic nie zmieniono")