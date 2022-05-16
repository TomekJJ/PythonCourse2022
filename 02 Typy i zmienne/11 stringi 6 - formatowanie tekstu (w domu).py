'''Przekopiuj zawartość import this do zmiennej.
    1. Policz liczbę wystąpień słowa better.
    2. Usuń z tekstu symbol gwiazdki
    3. Zamień jedno wystąpienie explain na understand
    4. Usuń spacje i połącz wszystkie słowa myślnikiem
    5. Podziel tekst na osobne zdania za pomocą kropki'''

# import
txt = '''Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!'''

'''
# 1. liczba powtórzeń
print('\n')
print(f'Ilośc powtórzeń słowa better', txt.count('better'))

# 2. Usuwanie gwiazdki
print('\n')
print('***USUWANIE GWIAZDKI***')
print(txt.replace('*', ''))

# 3.  Zamiana wyrazów
print('\n')
print('***ZAMIANA WYRAZÓW***')
print(txt.replace('explain', 'understand', 1))

# 4. myślniki za spacje
print('\n')
print('***MYŚLNIKI ZA SPACJE***')
print(txt.replace(' ', '-'))
'''
# 5. dzielenie tekstu (???????????)
txt2 = txt.rpartition('.')
print(txt2)