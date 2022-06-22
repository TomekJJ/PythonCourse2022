# Napisz program, który wyświetli kolejne wyniki dla silni liczby naturalnej N (N podane przez użytkownika, ale nie większe niż 8).

n = int(input('podaj liczbę od 1 do 8 -->'))


if n == 0:
    print("n silnia to ", 1)

elif n == 1:
    print('n silnia to ', 1)

else:
    s = 1
    for x in range(1, n):
        s = s * (x + 1)
    print("n silnia to ",  s)
