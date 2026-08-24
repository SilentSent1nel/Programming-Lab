líjst1 = []
lijst2 = []

def omgekeerde_lijst(lijst1, lijst2):
    for index in range(len(lijst1)):
        if lijst1[index] != lijst2[len(lijst2) - 1 - index]:
            return False
    return True

print(omgekeerde_lijst([1, 2, 3], [3, 2, 1]))
print(omgekeerde_lijst([1, 5, 3], [3, 2, 1]))