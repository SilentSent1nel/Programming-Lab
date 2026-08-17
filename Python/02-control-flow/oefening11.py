print("Ik heb informatie over de volgende planeten:\n")

print("   1. Venus   2. Mars    3. Jupiter")
print("   4. Saturnus  5. Uranus  6. Neptunus\n")
 
gewicht = 185
planeet = 3

if planeet == 1:
    gewicht = gewicht * 0.91
    print(gewicht)
elif planeet == 2:
    gewicht = gewicht * 0.38
    print(gewicht)
elif planeet == 3:
    gewicht = gewicht * 2.34
    print(gewicht)
elif planeet == 4:
    gewicht = gewicht * 1.06
    print(gewicht)
elif planeet == 5:
    gewicht = gewicht * 0.92
    print(gewicht)
else:
    gewicht = gewicht * 1.19
    print(gewicht)