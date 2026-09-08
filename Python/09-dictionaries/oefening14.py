beschikbare_items = {"gezondheidsdrank": 10, "genezingstaart": 5, "groen_elixer": 20, "kracht_sandwich": 25, "uithoudingsvermogen_granen": 15, "krachtstoofpot": 30}
gezondheidspunten = 20
gezondheidspunten = gezondheidspunten + beschikbare_items.pop("uithoudingsvermogen_granen", 0)

gezondheidspunten += beschikbare_items.pop("krachtstoofpot", 0)
gezondheidspunten += beschikbare_items.pop("mystiek_brood", 0)

print(beschikbare_items)
print(gezondheidspunten)