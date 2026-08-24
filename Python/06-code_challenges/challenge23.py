nummers = []

def maximale_getal(nummers):
    maxGetal = nummers[0]
    for getal in nummers:
        if getal > maxGetal:
            max = getal
    return max

print(maximale_getal([50, -10, 0, 75, 20]))