gewicht = 1.5
vaste_tarief = 20
premium_vaste_tarief = 125

# Verzending over land
if gewicht <= 2:
    prijs_per_kilo = 1.50
elif gewicht > 2 and gewicht <= 6:
    prijs_per_kilo = 3.00
elif gewicht <= 10:
    prijs_per_kilo = 4.00
else:
    prijs_per_kilo = 4.75

kosten = gewicht * prijs_per_kilo + vaste_tarief
print("Verzending over land: €", kosten)
print("Premium verzending over land vaste tarief €:",premium_vaste_tarief)

# Verzending per drone
if gewicht <= 2:
    drone_prijs_per_kilo = 4.50
elif gewicht > 2 and gewicht <= 6:
    drone_prijs_per_kilo = 9.00
elif gewicht <= 10:
    drone_prijs_per_kilo = 12.00
else:
    drone_prijs_per_kilo = 14.25

drone_verzending_kosten = gewicht * drone_prijs_per_kilo
print("Drone verzending: €", drone_verzending_kosten)