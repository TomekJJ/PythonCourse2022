txt = "abrakadabra"

for a in txt:
    print('-', a)

print('-------------------')
names = ["ada", "julia", "ruby"]
for k in names:
    print("hello",k)

print('-------------------')
for i in range(10):
    print('krok: ', i)

print('-------------------')
for i in range(5, 20, 2):
    print ('->', i)

print('-------------------')
for index in range(3):
    print(index, names[index])

print('-------------------')
for index, elem in enumerate(txt):
    print(index, elem)

print('-------------------')
len_txt = len(txt)
for i in range (0, len_txt, 2):
    print(i, txt[i])

print('-------------------')
pa = ""
magic = "hokuspokus"
for num in range (2, 10, 2):
    pa = pa + str(num) + magic[num]
    print(pa)

