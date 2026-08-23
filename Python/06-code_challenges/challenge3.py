# Hier de grote_macht functie:

def grote_macht(basis, exponent):
    if basis**exponent > 5000:
        return True
    else:
        return False

print(grote_macht(2, 13))
# zou True moeten printen

print(grote_macht(2, 12))
# zou False moeten printen