liedjes = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]
keren_afgespeeld = [78, 29, 44, 21, 89, 5]

gespeeld = {key:value for key, value in zip(liedjes, keren_afgespeeld)}

print(gespeeld)

gespeeld["Purple Haze"] = 1
gespeeld.update({"Respect": 94})

print(gespeeld)

bibliotheek = {"De beste liedjes": gespeeld, "Sunday Feelings": {}}
print(bibliotheek)