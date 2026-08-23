basissen = []
machten = []

def exponenten(basissen, machten):
    nieuwe_lijst = []
    for basis in basissen:
        for macht in machten:
            nieuwe_lijst.append(basis ** macht)
    return nieuwe_lijst

print(exponenten([2, 3, 4], [1, 2, 3]))