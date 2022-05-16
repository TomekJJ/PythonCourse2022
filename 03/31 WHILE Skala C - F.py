#  Napisz program zmieniający skalę w stopniach Fahrenheita na naszą w Celcjuszach.
#  Program powinen wykonać się w pętli od 0 do 200 stopni Fahrenheit, co 20 stopni.
#
# C = 5/9 * (F - 32) # wzór Celsjusz → Fahrenheit
#
# Napisz rozwiązanie zarówno z użyciem pętli while jak i for

far = 0

while(far < 200):
    print(far, "Fahr ->", round(5/9 * (far - 32), 2), "celc"   )
    far = far + 20

print("koniec")

