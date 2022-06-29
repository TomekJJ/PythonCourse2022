# Przypomnij sobie szkolny wzór na silnię.
# Zapisz funkcję silnia iteracyjnie np. pętlą for, a następnie analogiczną funkcję tylko, że rekurencyjnie.

def silnia_iteracyjnie(n):
    silnia = 1
    for i in range (2, n + 1):
        silnia *= i

    return silnia

def silnia_rekurencyjnie(n):
    if n > 1:
        return n * silnia_rekurencyjnie(n-1)
    else:
        return 1


n = int(input("n -> "))

print(f'{n}! to {silnia_iteracyjnie(n)}')
print(f'{n}! to {silnia_rekurencyjnie(n)}')