kapsels = ["volumineus", "pixie", "dreadlocks", "kort", "kom", "bob", "hanenkam", "platte top"]

prijzen = [30, 25, 40, 20, 20, 35, 50, 35]

vorige_week = [2, 3, 5, 8, 4, 4, 6, 2]


totale_prijs = 0
for prijs in prijzen:
    totale_prijs += prijs
print(totale_prijs)

gemiddelde_prijs = totale_prijs / len(prijzen)

print("Gemiddelde kappersprijs:", gemiddelde_prijs)
nieuwe_prijzen = [prijs - 5 for prijs in prijzen]

print("Nieuwe prijzen:", nieuwe_prijzen)
totale_omzet = 0

for i in range(len(kapsels)):
    totale_omzet += prijzen[i] * vorige_week[i]

print("Totale omzet:", totale_omzet)

gemiddelde_dagelijkse_omzet = totale_omzet / 7
print("Gemiddelde dagelijkse omzet:", gemiddelde_dagelijkse_omzet)

kapsels_onder_30 = []

for i in range(len(kapsels)):
    if nieuwe_prijzen[i] < 30:
        kapsels_onder_30.append(kapsels[i])

print("Kapsels onder 30:", kapsels_onder_30)