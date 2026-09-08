import csv

isbn_lijst = []

with open("boeken.csv") as boeken_csv:
    boeken_reader = csv.DictReader(boeken_csv, delimiter='@')

    for book in boeken_reader:
        isbn_lijst.append(book['ISBN'])


teller = 0
for boek in isbn_lijst:
    teller += 1
    print(f"{teller}. Boek ISBN: {boek}")