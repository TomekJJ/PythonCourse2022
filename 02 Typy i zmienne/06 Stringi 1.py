# Stwórz zmienną przechowującą wyraz o długości nieparzystej większej niż 7 i zwróć łańcuch złożony z trzech środkowych znaków danego ciągu.
word = input("podaj słowo")

print('Długość wyrazu: ', len(word))
mid  = len(word) // 2
mid  = int(mid)

prev = mid - 1
next = mid + 1

print(word[prev] + word [mid] + word [next])

print(word[prev:next+1])

