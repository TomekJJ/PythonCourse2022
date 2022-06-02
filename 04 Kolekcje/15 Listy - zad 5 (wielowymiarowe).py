# Utwórz “na sztywno” 2-wymiarową tablicę, tak, by kolejne wiersze zawierały dane osób, natomiast w kolumnach będzie znajdować się imię, nazwisko, zawód

tab = [
    ['Dorota', 'Welman', 'dziennikarka'],
    ['Adam', 'Małysz', 'sportowiec'],
    ['Robert', 'Lewandowski', 'piłkarz'],
    ['Krystyna', 'Janda', 'aktorka']
]
print(tab)
# najprościej
print("...........")
for person in tab:
    print(person)

# drugi sposób
print("...........")
for person in tab:
    print(*person)
    # gwiazdka rozpakowuje listę

# trzeci sposób
print("...........")
for person in tab:
        for index, value in enumerate(person):
                if index == 1:
                    print(value, end=" | ")
                else:
                    print(value, end=" ")
        print()
