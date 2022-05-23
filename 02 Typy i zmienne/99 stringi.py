txt = 'Python jest super!'
txt2 = " i już"

# mnożenie stringów
print(txt * 10 + " ")


# długość stringa
print(len(txt))

# pierwszy znak od lewej
print(txt[0])

# pierwszy znak od prawej
print(txt[-1])

# trzeci znak od lewej
print(txt[2])

# trzeci znak od prawej
print(txt[-3])

# zmienna[start:koniec:krok]
# Warto zauważyć start jest zawsze wyświetlany, a koniec zawsze pomijany, krok domyślnie wynosi 1.
# To zapewnia, txt[: i] + txt[i:] jest zawsze równe txt:

print(txt[0:5:1])

# całość
print(txt[0:])

# całość
print(txt[0:10])

# odwracanie  całości
print(txt[::-1])

# liczenie znaków
txt3 = "abrakadabra"
print(txt3.count("a"))
print(txt3.count("ab"))

# podmienienie znaków w stringu
txt4 = "Mata"
new_txt4 = "t" + txt4[1:]
print(new_txt4)

# podmienianie znaków w stringu drugi sposób
# replace nie nadpisuje zmiennej
print(txt4.replace("M", "t"))

# metody klas string - szykanie hel