filename = 'Pan_tadeusz2.txt'

with open(filename, 'r') as f:
  content = f.read()
  print(content)


# otwieranie linijka po linijce
print('.........................')
with open('Pan_tadeusz2.txt') as fopen:
    for line in fopen:
      print(line)

# na około z readline
# print('.........................')
# with open('Pan_tadeusz2.txt') as fopen:
#     while True:
#         currentline=fopen.readline()
#         print(fopen.readline())
#
#         if currentline == '':
#           break

with open('Pan_tadeusz2.txt') as fopen:
    print('.........................')
    content = fopen.readlines()

   print(content)
   for l in content:
     print(l)