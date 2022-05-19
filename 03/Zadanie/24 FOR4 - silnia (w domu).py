# Napisz program, który wyświetli kolejne wyniki dla silni liczby naturalnej N (N podane przez użytkownika, ale nie większe niż 8).

n = int(input('podaj liczbę od 1 do 8'))
x = 1

if n == 0:
    print(1)

if n == 1:
    print(1)

else:
    for x in range (1,n):
        x = x * (x + 1)
    print(x)
