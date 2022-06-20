# Wykorzystaj plik zawierający fragment Pana Tadeusza.
# Znajdź najdłuższe słowo występujące w zadanym fragmencie.

def remove_extras(tekst):
    for char in "!,.();":
            tekst = tekst.replace(char, '')

#    tekst = tekst.replace('\n', '')

    return tekst

def find_longer(tekst):
    longest = ''
    for word in tekst:
        if len(word) > len(longest):
            longest = word
    return longest

def main():
    with open('Pan_tadeusz2.txt', encoding='utf-8') as fopen:
        content = fopen.read()

    content = remove_extras(content)
    content = content.split() # dzielenie po domyślnym znaku
    longest_word = find_longer(content)
    print(longest_word)



main()