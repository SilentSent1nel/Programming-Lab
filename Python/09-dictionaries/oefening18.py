elementen = {1: "Waterstof", 2: "Helium", 3: "Lithium", 4: "Beryllium", 5: "Boor", 6: "Koolstof", 7: "Stikstof", 8: "Zuurstof", 9: "Fluor", 10: "Neon", 11: "Natrium", 12: "Magnesium", 13: "Aluminium", 14: "Silicium", 15: "Fosfor", 16: "Zwavel", 17: "Chloor", 18: "Argon", 19: "Kalium", 20: "Calcium", 21: "Scandium", 22: "Titanium"}

uitlezing = {}

uitlezing["katalysator"] = elementen.pop(6)
uitlezing["kern"] = elementen.pop(14)
uitlezing["bijproduct"] = elementen.pop(8)

print(uitlezing)

for sleutel, waarde in uitlezing.items():
    print(f"Jouw {sleutel}-element is {waarde}.")