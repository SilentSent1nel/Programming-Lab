def gebruikersnaam_generator(voornaam, achternaam):
    gebruikersnaam = voornaam[0:3] + achternaam[0:4]
    if len(voornaam) < 3 or len(achternaam) < 4:
        gebruikersnaam = voornaam + achternaam
    return gebruikersnaam

def wachtwoord_generator(gebruikersnaam):
    wachtwoord = ""

    for i in range(0, len(gebruikersnaam)):
        wachtwoord += gebruikersnaam[i - 1]
    return wachtwoord

print(wachtwoord_generator("AbeSimp"))