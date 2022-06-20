with open ('tekst.txt', 'w') as f:
    f.write("Litwo. Ojczyzno Moja, Ty jesteś jak zdrowie, ile cię trzeba cenić...")

filename = 'tekst.txt'

with open(filename, 'r') as f:
  content = f.read()
  print(content)