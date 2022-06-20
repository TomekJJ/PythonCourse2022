def find_longest_word(sequence):
    """Finds the longest element in a sequence"""
    longest_word = ''
    for word in sequence:
        if len(word) > len(longest_word):
            longest_word = word

    return longest_word


def show(text):
    print('*****')
    print(text.center(10))
    print('*****')


text = 'abrakadabra'
print(text)
print(find_longest_word(['ala', 'ma', 'pieski']))

