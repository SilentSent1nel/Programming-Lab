def zelfde_naam(jouw_naam, mijn_naam):
    if jouw_naam == mijn_naam:
        return True
    else:
        return False

print(zelfde_naam("Agrîn", "Agrîn"))
# Zou "True" moeten printen

print(zelfde_naam("Navdar", "Zozan"))
# Zou "False" moeten printen