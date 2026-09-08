import csv

with open ("leuke_csv.csv") as leuke_csv_bestand:
    leuke_csv_dict = csv.DictReader(leuke_csv_bestand)

    for rij in leuke_csv_dict:
        print(rij['Cool Fact'])