print('.........')
hobbits = ['sam', 'frodo', 'pippin']
grades = ['1', '2', '3', '4', '5']

# dodawanie list
print(hobbits + grades)

print(hobbits[1])
    # zawsze liczymy od zera

# modyfikowanie list
hobbits[1] = 'tomek'

hobbits.append("ola")

hobbits.insert(1, "ola")

print(hobbits)

print('.........')
veggies = ['carrot', 'kale', 'peas']
print(veggies)
# usuwanie elementu po wartości
veggies.remove('kale')
print(veggies)
#usuwanie elementu po indeksie
del veggies[1]
    #del usuwa dowolny obiekt (zawartość listy lub całą liste)
print(veggies)


print('.........')
print(list(range(10)))
