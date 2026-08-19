voorraad = ["twin bed", "twin bed", "headboard", "queen bed", "king bed", "dresser", "dresser", "table", "table", "nightstand", "nightstand", "king bed", "king bed", "twin bed", "twin bed", "sheets", "sheets", "pillow", "pillow"]
lengte_voorraad = len(voorraad)

print(lengte_voorraad)
eerste = voorraad[0]

laatste = voorraad[-1]
voorraad_2_6 = voorraad[2:6]

print(voorraad_2_6)
eerste_3 = voorraad[0:3]

tweepersoons_bedden = voorraad.count("twin bed")
print(tweepersoons_bedden)

verwijderd_item = voorraad.pop(4)
print(verwijderd_item)

voorraad.insert(10, "19th Century Bed Frame")
print(voorraad)

voorraad.sort()
print(voorraad)