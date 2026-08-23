mijn_lijst = []

def verwijder_beginnende_evengetallen(mijn_lijst):
    while (len(mijn_lijst) > 0 and mijn_lijst[0] % 2 == 0):
        mijn_lijst = mijn_lijst[1:]
    return mijn_lijst

print(verwijder_beginnende_evengetallen([4, 8, 10, 11, 12, 15]))
print(verwijder_beginnende_evengetallen([4, 8, 10]))