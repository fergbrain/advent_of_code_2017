import csv
from collections import Counter

puzInput = list(csv.reader(open('input', 'rb'), delimiter=' '))

# https://stackoverflow.com/questions/11236006/identify-duplicate-values-in-a-list-in-python

duplicate_count = 0

for row in puzInput:
    if len(([k for k, v in Counter(row).items() if v > 1])) > 0:
        duplicate_count += 1


print len(puzInput) - duplicate_count
