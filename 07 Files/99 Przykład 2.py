# with open('save.txt', 'w') as f:
#   f.write('Line 1')
#   f.write('Line 2')
#   f.write('Line 3')
#   f.write('Line 4')


with open('save.txt', 'w') as f:
  f.write('wiersz 5\n')
  f.write('wiersz 6\n')
  f.write('wiersz 7\n')
  f.write('wiersz 8\n')
  f.write('The end!')

with open('save.txt', 'r') as f:
  lines = f.readlines()

  for l in range(len(lines)):
    print(lines[l])