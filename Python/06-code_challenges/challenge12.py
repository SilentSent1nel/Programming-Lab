mijn_lijst = []

def som_toevoegen(mijn_lijst):
    for x in range(len(mijn_lijst)):
        mijn_lijst.append(mijn_lijst[-1] + mijn_lijst[-2])
    return mijn_lijst

print(som_toevoegen([1, 1, 2]))