"""
Je krijgt een maandelijks budget en een aantal uitgaven. 
Je moet controleren of de som van de uitgaven het budget overschrijdt

Sla eerst het totaal van alle uitgaven op in een variabele genaamd `total`.

Controleer vervolgens of het totaal hoger is dan het budget. 
Zo ja, sla dan `True` op in een variabele genaamd `over_budget`, 
anders sla je `False` op in `over_budget`.
"""

# Maandelijkse budget
budget = 2000

# Maandelijkse uitgaven
voedsel_rekening = 200
elektriciteit_rekening = 100
internet_rekening = 60
huur = 1500

# Bereken de totale uitgaven per maand
totaal = voedsel_rekening + elektriciteit_rekening + internet_rekening + huur

# Check of het totaalbedrag hoger is dan het budget en sla het resultaat op in "over_budget"

if totaal > budget:
  over_budget = True
else:
  over_budget = False

print("Totaal: " + str(totaal))
print("Is het budget overschreden? " + str(over_budget))
print("Overgebleven budget:",budget - totaal)
