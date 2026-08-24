def hondenjaren(naam, leeftijd):
    hondenleeftijd = leeftijd * 7
    resultaat = naam + ', ' + 'je bent ' + str(hondenleeftijd) + ' jaar oud in hondenjaren'
    return resultaat

print(hondenjaren("Milo", 16))
print(hondenjaren("Luna", 0))
print(hondenjaren("Toby", 5))
print(hondenjaren("Coca", 12))