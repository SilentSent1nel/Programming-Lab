def bereken_kosten(vliegticket_prijs, autohuur_tarief, hotel_tarief, verblijfsduur):
    totale_autohuur = autohuur_tarief * verblijfsduur
    totaal_hotel = hotel_tarief * verblijfsduur - 10
    totale_reiskosten = totale_autohuur + totaal_hotel + vliegticket_prijs
    return totale_reiskosten

vliegticket_prijs = 200
autohuur_tarief = 100
hotel_tarief = 100
verblijfsduur = 5

print(bereken_kosten(vliegticket_prijs, autohuur_tarief, hotel_tarief, verblijfsduur))