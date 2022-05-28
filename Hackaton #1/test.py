pswrd = "tomek"
ingame_pswrd =[]
letter = input("Zgadnij literę -->")

if letter in pswrd:
    for i, v in enumerate(pswrd):  # i to indeks, v to wartość
        if letter == v:
            ingame_pswrd[i] = letter
    print(ingame_pswrd)
else:
    print("W haśle nie ma takiej litery")