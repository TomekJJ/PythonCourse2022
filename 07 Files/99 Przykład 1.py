# tu coś z początku zajęć


# with open ('pan_tadeusz') as f:
#    print(f.readline())

with open('nowy_plik', 'a+') as f:
    f.write('\n' +'nowe dane')


with open('nowy_plik', 'r') as f:
    content = f.read()
    print(content)
