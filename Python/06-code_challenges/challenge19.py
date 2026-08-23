mijn_lijst = []


def oneven_indices(mijn_lijst):
    nieuwe_list = []
    for index in range (1, len(mijn_lijst), 2):
        nieuwe_list.append(mijn_lijst[index])
    return nieuwe_list

print(oneven_indices([4, 3, 7, 10, 11, -2]))