lijst1 = []
lijst2 = []

def grotere_som(lijst1, lijst2):

    som1 = 0
    som2 = 0

    for num in lijst1:
        som1 += num
    for num in lijst2:
        som2 += num
    if som1 >= som2:
        return lijst1
    else:
        return lijst2

print(grotere_som([1, 9, 5], [2, 3, 7]))