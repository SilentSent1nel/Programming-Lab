verkoopgegevens = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]

verkochte_bollen = 0

for locatie in verkoopgegevens:
    print(locatie)
    for bol in locatie:
        verkochte_bollen += bol

print(verkochte_bollen)