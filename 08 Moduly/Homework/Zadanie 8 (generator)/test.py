import random

seq = [0,1,2,4,5,6,7,8,9]
n = 8

def generate_pass(seq, n):
    passw = []
    for i in range(n):
        a = random.choice(seq)
        passw.append(a)


    return passw


def main():
    result = generate_pass(seq, n)
    print("Losowe hasło to; ",  *result)
main()