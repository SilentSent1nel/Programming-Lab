aantal_oefeningen = {"functies": 10, "syntaxis": 13, "controle_stroom": 15, "lussen": 22, "lijsten": 19, "klassen": 18, "woordenboeken": 18}
totaal_oefeningen = 0

for oefeningen in aantal_oefeningen.values():
    totaal_oefeningen += oefeningen

print(totaal_oefeningen)