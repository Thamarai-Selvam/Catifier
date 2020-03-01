
import csv

animals = open("animals.txt").read().split("\n")

animals.sort()
with open('animals.csv', 'w', newline = '') as file :
    w = csv.writer(file)
    w.writerow(["animalNames"])
    for name in animals:
        w.writerow([name])

print('CSV Created...')

