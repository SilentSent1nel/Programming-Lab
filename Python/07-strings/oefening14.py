auteurs = "Audre Lorde,Gabriela Mistral,Jean Toomer,An Qi,Walt Whitman,Shel Silverstein,Carmen Boullosa,Kamala Suraiyya,Langston Hughes,Adrienne Rich,Nikki Giovanni"

auteurs_namen = auteurs.split(",")
auteurs_achternamen = []

for achternaam in auteurs_namen:
    achternaam = achternaam.split(" "[-1])
    auteurs_achternamen.append(achternaam[-1])


print(auteurs_namen)
print(auteurs_achternamen)