import csv
from pprint import pprint

EINSTEIN_CSV = 'Albert,Einstein,1879-03-14,1955-04-18,Germany,"for his services to Theoretical Physics, and especially for his discovery of the law of the photoelectric effect",physics,1921'

EINSTEIN = {
    "birthplace": "Germany",
    "name": "Albert",
    "surname": "Einstein",
    "born": "1879-03-14",
    "category": "physics",
    "motivation": "for his services to Theoretical Physics...",
}

with open("laureates.csv", "r") as f: # opens csv file and use read mode, f - file
    reader = csv.DictReader(f)
    laureates = list(reader)

for laureate in laureates: # for each laureate in the laureates
    if laureate["surname"] == "Einstein":
        pprint(laureate)
        break
