def veel_wiskunde(a, b, c, d):
    eerste_resultaat = (a + b)
    tweede_resultaat = (c - d)
    derde_resultaat = eerste_resultaat * tweede_resultaat
    vierde_resultaat = derde_resultaat % a

    print(eerste_resultaat)
    print(tweede_resultaat)
    print(derde_resultaat)

    return vierde_resultaat

print(veel_wiskunde(1, 2, 3, 4))
print(veel_wiskunde(1, 1, 1, 1))