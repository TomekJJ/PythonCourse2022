import math

fibonacci = []
n = 5
for n in range(0, n):
    f_n = int(1 / math.sqrt(5) * ((1 + math.sqrt(5)) / 2)**n - 1 / math.sqrt(5) * ((1 - math.sqrt(5)) / 2)**n)
    fibonacci.append(f_n)

print(fibonacci)
