# Pobierz od użytkownika dowolny tekst i
# wyświetl tylko te znaki, które są na pozycjach parzystych.
# Wykonaj na dwa sposoby - za pomocą pętli oraz przez sting slicing ( ‘abrakadabra’ -> ‘baaar’).

txt = "abrakadabra"
i = 0

# za pomocą for
lista1 = []
for i, e in enumerate(txt,start=1):
    if i % 2 == 0:
        lista1.append(e)
print(lista1)


# za pomocą string slicing
print(txt[1::2])
