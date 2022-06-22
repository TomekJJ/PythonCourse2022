
def find_longest(var):
    longest_seq = []
    curr_seq = []

    for index, elem in enumerate(var):
        if var[index] == var[index - 1] and var[index-1] == var[index - 2]:
            curr_seq.append(elem)
        elif var[index] == var[index - 1]:
            curr_seq.append(elem)
        else:
            if len(curr_seq) > len(longest_seq):
                longest_seq = curr_seq
            else:
                curr_seq = []

    return longest_seq


def main():
    var = 'banannnnannnnnnnnnanananananaaaana'

    result = find_longest(var)
    print(*result, ",", len(result))
    print(f'najdłuższa sekwencja znaków w podanym ciągu to "{result}". Składa się z {len(result)} znaków')


main()
