cijfers_vorig_semester = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

vakken = ["physics", "calculus", "poetry", "history"]
cijfers = [98, 97, 85, 88]

cijferlijst = [["physics", 98], ["calculus", 97], ["poetry", 85], ["history", 88]]
print(cijferlijst)

vakken.append("computer science")
cijfers.append(100)

cijferlijst.append(["computer science"])
cijferlijst[4].append(100)

print(vakken)
print(cijfers)

print(cijferlijst)

vakken.append("visual arts")

cijfers.append(93)
cijferlijst.append(["visual arts"])

cijferlijst[5].append(93)
print(vakken)

print(cijfers)
print(cijferlijst)

correctie_cijfer_visuele_kunst = cijfers[-1] = 98
correctie_cijfer_visuele_kunst = cijferlijst[5][1] = cijferlijst[5][1] + 5

print(cijfers)
print(cijferlijst)

cijferlijst[2].remove(85)
print(cijferlijst)

cijferlijst[2].append("Pass")
print(cijferlijst)


volledige_cijferlijst = cijfers_vorig_semester + cijferlijst
print(volledige_cijferlijst)