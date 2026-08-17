statement_1 = not (4 + 5 <= 9)

statement_2 = not (8 * 2) != 20 - 4

punten = 120
gpa = 1.8

if not punten >= 120:
    print("Je hebt geen genoeg punten om te afstuderen.")
if not gpa >= 2.0:
    print("Je GPA is niet hoog genoeg om te afstuderen.")
if not punten >= 120 and not gpa >= 2.0:
    print("Je voldoet aan geen van beide eisen om te afstuderen!")