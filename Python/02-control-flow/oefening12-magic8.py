import random

naam = "S-Sentinel"
vraag = "Gaat het vandaag regenen?"
antwoord = ""

random_number = random.randint(1, 11)

if vraag == "":
    print("What is your vraag?")
else:
    if naam == "":
        print("Vraag: ",vraag)
    else:
        print(naam, "asks:", vraag)

    if random_number == 1:
        print("Magische 8-Ball's antwoord: Ja - absoluut")
    elif random_number == 2:
        print("Magische 8-Ball's antwoord: Dat is beslist zo")
    elif random_number == 3:
        print("Magische 8-Ball's antwoord: Zonder twinfel")
    elif random_number == 4:
        print("Magische 8-Ball's antwoord: Antwoord onduidelijk, probeer het opnieuw")
    elif random_number == 5:
        print("Magische 8-Ball's antwoord: Vraag het later nog eens")
    elif random_number == 6:
        print("Magische 8-Ball's antwoord: Ik kan het je nu beter niet vertellen")
    elif random_number == 7:
        print("Magische 8-Ball's antwoord: Mijn bronnen zeggen nee")
    elif random_number == 8:
        print("Magische 8-Ball's antwoord: Vooruitzichten niet zo best")
    elif random_number == 9:
        print("Magische 8-Ball's antwoord: Zeer twijfelachtig")
    elif random_number == 10:
        print("Magische 8-Ball's antwoord: Er is een kans")
    elif random_number == 11:
        print("Magische 8-Ball's antwoord: Volgens mijn bronnen, waarschijnlijk niet")
    else:
        antwoord = "Fout"
        print(antwoord)

