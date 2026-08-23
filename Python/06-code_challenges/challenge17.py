namen = []

def voeg_groeten_toe(namen):
    groeten = []
    for naam in namen:
        groeten.append("Hallo, " + naam)

    return groeten

print(voeg_groeten_toe(["Owen", "Max", "Sophie"]))