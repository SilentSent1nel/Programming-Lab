def bevat(grote_tekst, kleine_tekst):
    if kleine_tekst in grote_tekst:
        return True
    return False

def gemeenschappelijke_letters(tekst_een, tekst_twee):
    lijst = []
    for teken in tekst_een:
        if teken in tekst_twee and teken not in lijst:
            lijst.append(teken)
    return lijst

print(gemeenschappelijke_letters("banaan", "aardbei"))