# Modules
import datetime as dt
from decimal import Decimal
from random import randint, choice
import custom_module
# -----------------------------------------------

#  Code


# Datum van vandaag
TijdNu = dt.datetime.now()
TijdNu = TijdNu.strftime("%H:%M:%S")

DatumNu = dt.datetime.now()
DatumNu = DatumNu.strftime("%d-%m-%Y")

# Willekeurige jaar
WillekeurigeJaar = randint(2050, 2090)

# Tijdreis kosten berekening
basiskosten = Decimal('150.00')
vermenigvuldiger = Decimal('25.00')
DoelJaar = WillekeurigeJaar
HuidigeJaar = dt.datetime.now().year
VerschilInJaren = abs(DoelJaar - HuidigeJaar)
extra_kosten = VerschilInJaren * vermenigvuldiger
eindkosten = basiskosten + extra_kosten


# Willekeurige selecties
mogelijke_bestemmingen = ['Pluto', 'de Maan', 'de Aarde', 'de Zon']
BestemmingsKeuze = choice(mogelijke_bestemmingen)

# Eind uitvoer
print(custom_module.genereer_tijds_reis_bericht(WillekeurigeJaar, BestemmingsKeuze, f"{eindkosten:.2f}"))