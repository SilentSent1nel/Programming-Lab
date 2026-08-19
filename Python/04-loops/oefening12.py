# Jouw code hieronder:
enkele_cijfers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
kwadraten = []

for cijfer in enkele_cijfers:
    print(cijfer)
    kwadraten.append(cijfer**2)

print(enkele_cijfers)
print(kwadraten)

kubussen = [cijfer ** 3 for cijfer in enkele_cijfers]
print(kubussen)