voornaam = "Agrîn"
achternaam = "Welat"

def account_generator(voornaam, achternaam):
    nieuwe_account = voornaam[0:3] + achternaam[0:3]
    return nieuwe_account

nieuwe_account = account_generator(voornaam, achternaam)
print(nieuwe_account)