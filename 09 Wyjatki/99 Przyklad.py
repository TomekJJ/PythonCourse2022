x = 35 - 6
print(x)

try:
    ppl = int(input('podaj liczbe osób ->'))
    result = 10 / ppl

except ZeroDivisionError as err:
    print('Pojawił sie błąd. Twój wyjątek to', err)
    result = 10
except ValueError:
    print("Nowy bład!!!!")
    result = 10


print(result)
print("The end")
