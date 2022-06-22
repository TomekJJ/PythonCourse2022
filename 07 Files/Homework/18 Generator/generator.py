import random


def upload_file():
    with open('generator.csv', encoding='utf-8-sig') as f:
        content = f.readlines()
        prefixy = []
        middle1 = []
        middle2 = []
        sufixy = []

        for l in content:
            frazy = l.split(';')
            prefixy.append(frazy[0])
            middle1.append(frazy[1])
            middle2.append(frazy[2])
            sufixy.append(frazy[3])

    return prefixy, middle1, middle2, sufixy


def get_random(lista):
    quote = random.choice(lista)
    return quote


def main():
    prefixy, middle1, middle2, sufixy = upload_file()

    phrase = get_random(prefixy) + " " + get_random(middle1) + " " + get_random(middle2) + " " + get_random(sufixy)
    print(phrase)

    print(prefixy)
    print(middle1)


main()
