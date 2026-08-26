voornaam = "Agrîn"
achternaam = "Welat"

def wachtwoord_generator(voornaam, achternaam):
    laatste_3_letters = voornaam[len(voornaam)-3:] + achternaam[len(achternaam)-3:]
    return laatste_3_letters

tijdelijke_wachtwoord = wachtwoord_generator(voornaam, achternaam)
print(tijdelijke_wachtwoord)