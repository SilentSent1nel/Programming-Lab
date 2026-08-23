mijn_lijst = []

def meer_dan_n(mijn_lijst, item, n):
    if mijn_lijst.count(item) > n:
        return True
    else:
        return False

print(meer_dan_n([2, 4, 6, 2, 3, 2, 1, 2], 2, 3))