with open('slechte_bands.txt', 'w') as slechte_bands_doc:
    slechte_bands_doc.write("Bad Boy Records")

with open('slechte_bands.txt') as slechte_bands_doc:
    for line in slechte_bands_doc:
        print(line)