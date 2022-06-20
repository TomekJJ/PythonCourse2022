# Wyświetl tylko 5 pierwszych linii

with open('cytaty.txt', encoding='utf-8') as fopen:
    lines = fopen.readlines()

    for l in range(3):
        print(lines[l])