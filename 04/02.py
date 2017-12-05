import csv
from collections import Counter

puzInput = list(csv.reader(open('input', 'rb'), delimiter=' '))

# https://stackoverflow.com/questions/11236006/identify-duplicate-values-in-a-list-in-python

duplicate_count = 0

for i in range(0,len(puzInput)):
    for j in range(0,len(puzInput[i])):
        puzInput[i][j] = ''.join(sorted(puzInput[i][j]))


for row in puzInput:
    if len(([k for k, v in Counter(row).items() if v > 1])) > 0:
        duplicate_count += 1


print len(puzInput) - duplicate_count

