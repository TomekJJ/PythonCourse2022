# Stwórz dwie zmienne s1 i s2 przechowujące dowolne wyrazy, utwórz nowy łańcuch s3, dołączając s2 w środku s1.

s1 = "Dzień"
s2 = "niepodległości"

mid_s1 = len(s1) // 2

#ze spacjami
print(s1[0:mid_s1],s2,s1[mid_s1:])

#bez spacji
new_world = s1[0:mid_s1] + s2 + s1[mid_s1:]
print(new_world)

