def gedicht_beschrijving(publicatiedatum, auteur, titel, oorspronkelijk_werk):
  gedicht_beschrijving = "Het gedicht {titel} van {auteur} werd oorspronkelijk gepubliceerd in {oorspronkelijk_werk} in {publicatiedatum}.".format(publicatiedatum = publicatiedatum, auteur = auteur, titel = titel, oorspronkelijk_werk = oorspronkelijk_werk)
  return gedicht_beschrijving

auteur = "Shel Silverstein"
titel = "My Beard"
oorspronkelijk_werk = "Where the Sidewalk Ends"
publicatiedatum = "1974"

mijn_baard_beschrijving = gedicht_beschrijving(publicatiedatum, auteur, titel, oorspronkelijk_werk)
print(mijn_baard_beschrijving)