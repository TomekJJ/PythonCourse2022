# Usuń duplikat z podanej list i utwórz na jej bazie krotkę. Znajdź minimalną i maksymalną liczbę w krotce

example_list = [34, 17, 25, 41, 12, 194, 41, 3, 12, 99, 94]

set_bez_dupl = set(example_list)
tuple_bez_dupl = tuple(set_bez_dupl)

max_value = max(tuple_bez_dupl)
min_value = min(tuple_bez_dupl)

print("bez duplikatów ->", tuple_bez_dupl)
print("max ->", max_value)
print("min ->", min_value)
