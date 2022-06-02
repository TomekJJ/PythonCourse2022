# W wierszu policz wystąpienie każdego wyrazu, zignoruj wielkość liter.

txt = """Szybko, zbudź się, szybko, wstawaj
Szybko, szybko, stygnie kawa
Szybko, zęby myj i ręce"""

txt2 = txt.replace(',','')
txt3 = txt2.lower()

words = txt3.split()

words_counter = {}

for word in words:
    if word in words_counter:
        words_counter[word] += 1
    else:
        words_counter[word] = 1

print(words_counter)

for k, v in words_counter.items():
    print(f'- {k} : {v}')
