regels = [
    '  Ik ben vandaag naar de supermarkt geweest  ',
    '  Daarna heb ik mijn huis opgeruimd  ',
    'en een film gekeken  ',
    '  voordat ik ging slapen  ',
    '\n',
    '  Einde van de dag  '
]

opgeschoonde_regels = []

for regel in regels:
    opgeschoonde_regels.append(regel.strip())

volledige_tekst = '\n'.join(opgeschoonde_regels)

print(volledige_tekst)