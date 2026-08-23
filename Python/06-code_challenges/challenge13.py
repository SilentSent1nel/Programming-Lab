mijn_lijst1 = []
mijn_lijst2 = []

def grotere_lijst(mijn_lijst1, mijn_lijst2):
    if len(mijn_lijst1) >= len(mijn_lijst2):
        return mijn_lijst1[-1]
    else:
        return mijn_lijst2[-1]

print(grotere_lijst([4, 10, 2, 5], [-10, 2, 5, 10]))