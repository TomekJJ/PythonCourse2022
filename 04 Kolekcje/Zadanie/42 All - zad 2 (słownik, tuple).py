# Utwórz listę lub krotkę tuples_to_dict zawierającą krotki 2 elementowe. Przekształć ją w słownik dict_from_tuples.

tuples_to_dict = (('Tomek', 'Andrzej'), ('Ola', 'Maja'), ('Henio', 'Paweł'))

dict_from_tuples = dict(tuples_to_dict)

print('Lista krotek', tuples_to_dict)
print('słownik', dict_from_tuples)

print('...........')

dict_from_tuples['Kazio'] = "Jan"

print(dict_from_tuples)

new_dict = {}.fromkeys(["Ola", 'Tomek', 'Henio'], 3)
print(new_dict)