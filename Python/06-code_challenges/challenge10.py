def grootste_getal(getal1, getal2, getal3):
    if getal1 > getal2 and getal1 > getal3:
        return getal1
    elif getal2 > getal1 and getal2 > getal3:
        return getal2
    elif getal3 > getal1 and getal3 > getal2:
        return getal3
    else:
        return "Het is gelijkspel!"

# zou 10 moeten printen
print(grootste_getal(-10, 0, 10))

# zou 5 moeten printen
print(grootste_getal(-10, 5, -30))

# zou -5 moeten printen
print(grootste_getal(-5, -10, -10))

# zou "Het is gelijkspel!" moeten printen
print(grootste_getal(2, 3, 3))