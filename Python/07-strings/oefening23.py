uitgelichte_gedichten = "Afterimages:Audre Lorde:1997,  The Shadow:William Carlos Williams:1915, Ecstasy:Gabriela Mistral:1925,   Georgia Dusk:Jean Toomer:1923,   Parting Before Daybreak:An Qi:2014, The Untold Want:Walt Whitman:1871, Mr. Grumpledump's Song:Shel Silverstein:2004, Angel Sound Mexico City:Carmen Boullosa:2013, In Love:Kamala Suraiyya:1965, Dream Variations:Langston Hughes:1994, Dreamwood:Adrienne Rich:1987"

uitgelichte_gedichten_lijst = uitgelichte_gedichten.split(",")
uitgelichte_gedichten_zonder_spaties = []

for gedicht in uitgelichte_gedichten_lijst:
    gedicht.strip()
    zonder_spaties = gedicht.strip()
    uitgelichte_gedichten_zonder_spaties.append(zonder_spaties)

uitgelichte_gedichten_details = []

for zonder_spaties in uitgelichte_gedichten_zonder_spaties:
    opgesplitst = zonder_spaties.split(":")
    uitgelichte_gedichten_details.append(opgesplitst)

titels = []
dichters = []
datums = []

for details in uitgelichte_gedichten_details:
    titels.append(details[0])
    dichters.append(details[1])
    datums.append(details[2])


for i in range(len(titels)):
    print("Het gedicht {} werd gepubliceerd door {} in {}".format(titels[i], dichters[i], datums[i]))