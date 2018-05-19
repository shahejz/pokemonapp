import csv
from itertools import islice

with open("pokemon.csv") as f:
    reader = csv.DictReader(f)
    for row in islice(reader, 0, 50):
        print (row['name'], row['type1'], row['type2'])