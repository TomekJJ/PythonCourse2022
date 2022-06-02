# Napisz skrypt, który podaną listę podzieli na 3 równe listy i odwraca każdą z tych.

inpt = [1, 2, 3, 4, 11, 12, 13, 14, 21, 22, 23, 24]

output1 = inpt[0:4]
output2 = inpt[4:8]
output3 = inpt[8:13]

output1.reverse()
output2.reverse()
output3.reverse()

print(output1)
print(output2)
print(output3)
