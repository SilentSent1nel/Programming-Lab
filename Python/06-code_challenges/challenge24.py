lijst1 = []
lijst2 = []

def zelfde_waarden(lijst1, lijst2):
    nieuwe_lst = []
    for index in range(len(lijst1)):
        if lijst1[index] == lijst2[index]:
            nieuwe_lst.append(index)

    return nieuwe_lst

print(zelfde_waarden([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))