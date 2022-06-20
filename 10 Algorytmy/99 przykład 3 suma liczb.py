# z pętlą for
def sum_natural_for(n):
    sum_num = 0

    for i in range(1, n+1):
        sum_num += i

    return sum_num

# z pętlą while
def sum_natural_while(n):
    sum_num = 0

    while n >= 1:
        sum_num += n
        n -= 1

    return sum_num

# z rekurencją
def sum_natural_rek(n):
    if n == 1:
        return 1
    return n + sum_natural_rek(n - 1)


print(sum_natural_for(10))
print(sum_natural_while(10))
print(sum_natural_rek(10))
