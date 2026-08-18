# Jouw code hieronder:
voornamen = ["Ainsley", "Ben", "Chani", "Depak"]
voorkeursmaat = ["Small", "Large", "Medium"]

voorkeursmaat.append("Medium")
print(voorkeursmaat)


klantgegevens = [["Ainsley", "Small", True], ["Ben", "Large", False], ["Chani", "Medium", True], ["Depak", "Medium", False]]
print(klantgegevens)

chani_verzending_wijzigen = klantgegevens[2][2] = False
print(klantgegevens)

klantgegevens[1].remove(False)
print(klantgegevens)

uiteindelijke_klantgegevens = klantgegevens + [["Amit", "Large", True], ["Karim", "X-Large", False]]
print(uiteindelijke_klantgegevens)