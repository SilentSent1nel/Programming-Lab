voornamen = ["Ainsley", "Ben", "Chani", "Depak"]
voorkeursmaat = ["Small", "Large", "Medium"]

voorkeursmaat.append("Medium")
print(voorkeursmaat)


klantgegevens = [["Ainsley", "Small", True], ["Ben", "Large", False], ["Chani", "Medium", True], ["Depak", "Medium", False]]
print(klantgegevens)

chani_verzendvoorkeur_wijzigen = klantgegevens[2][2] = False
print(klantgegevens)

klantgegevens[1].remove(False)
print(klantgegevens)