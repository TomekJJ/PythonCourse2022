# Pozwól użytkownikowi wprowadzić dowolną liczbę imion ciągiem (np.jako jeden string rozdzielonych przecinkiem lub białym znakiem).
# Następnie powitaj każdą osobę na liście.

lista = input("podaj imiona jako listę rozdzielając je wyłącznie przecinkiem")
lista_mod = lista.split(',')

for i in lista_mod:
    print ("hello", i)

