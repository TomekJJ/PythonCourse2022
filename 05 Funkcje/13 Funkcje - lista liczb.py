# Napisać funkcję, która przyjmuje listę liczb i zwraca sumę wszystki elementów na liście.

def sumuj_elementy_listy(array):
    return sum(array)

array = [1,2,3,4,5]
#  = list(input('podaj listę liczb -->'))
# array1 = array.split(', ')

result = sumuj_elementy_listy(array)
print(result)