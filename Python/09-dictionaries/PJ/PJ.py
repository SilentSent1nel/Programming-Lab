letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
punten = [1, 2, 2, 2, 1, 3, 3, 3, 1, 4, 3, 1, 2, 3, 1, 3, 5, 1, 1, 1, 2, 3, 3, 4, 3, 5]

letter_naar_punten = {key:value for key, value in zip(letters, punten)}


def woord_score(woord):
    totaal_punten = 0

    for letter in woord:
        totaal_punten += letter_naar_punten.get(letter, 0)

    return totaal_punten

brownie_punten = woord_score("BROWNIE")
#print(brownie_punten)

speler_naar_woorden = {"player1": ["BLUE", "TENNIS", "EXIT"], "wordNERD": ["EARTH", "EYES", "MACHINE"], "Lexi Con": ["ERASER", "BELLY", "HUSKY"], "Prof Reader": ["ZAP", "COMA", "PERIOD"]}
speler_naar_punten = {}

for speler, woorden in speler_naar_woorden.items():
    speler_punten = 0

    for woord in woorden:
        woord_score(woord)
        speler_punten += woord_score(woord)
    speler_naar_punten[speler] = speler_punten

print(speler_naar_punten)