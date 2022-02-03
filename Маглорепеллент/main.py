import json
import csv

f = open("muggle_repellent.json")
creatures = json.load(f)
f.close()

f = open('muggle_magic.csv', 'w')
writer = csv.writer(f)
writer.writerow(["name", "size", "danger", "magic", "additional"])

data = []
for creature in creatures:
    name = creature["creature"]
    size = creature["size"]
    danger = creature["danger"]
    magic = creature["magic"]

    additional = 100 - size * magic // danger
    if additional < 0:
        additional = 0

    data.append([name, size, danger, magic, additional])

data = sorted(data, key=lambda e: (-e[4], e[0]))
for creature in data:
    writer.writerow(creature)

f.close()
