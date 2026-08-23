mijn_lijst1 = []
mijn_lijst2 = []

def combineer_sorteren(mijn_lijst1, mijn_lijst2):
    gecombineerde_lijsten = mijn_lijst1 + mijn_lijst2

    return sorted(gecombineerde_lijsten)


print(combineer_sorteren([4, 10, 2, 5], [-10, 2, 5, 10]))