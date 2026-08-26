def krijg_lengte(tekst):
    teller = 0
    for teken in tekst:
        teller += 1
    return teller

test = "S-Sentinel"
print(krijg_lengte(test))