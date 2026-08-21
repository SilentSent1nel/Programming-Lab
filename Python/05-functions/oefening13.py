def reisplanner_welkom(naam):
    print("Welkom bij tripplanner v1.0", naam)

reisplanner_welkom("S-Sentinel")

def geschatte_tijd_afgerond(geschatte_tijd):
    afgeronde_tijd = round(geschatte_tijd)
    return afgeronde_tijd

schatting = geschatte_tijd_afgerond(2.7)

def bestemming_instellen(vertrekpunt, bestemming, geschatte_tijd, vervoermiddel="Auto"):
    print("Je reis begint in", vertrekpunt)
    print("En je reist naar", bestemming)
    print("Je reist met", vervoermiddel)
    print("Het duurt ongeveer", str(geschatte_tijd), "uur")

bestemming_instellen("Düsseldorf", "Hewlêr", schatting, "Vliegtuig")