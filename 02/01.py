import csv

puzInput = list(csv.reader(open('input', 'rb'), delimiter='\t'))

checksum = 0

for row in puzInput:
    #print row
    maxVal = int(row[0])
    minVal = int(row[0])
    
    for cell in row:
        #print "Testing %d against max: %d and min: %d" % (int(cell), maxVal, minVal)
        if int(cell) < minVal:
            minVal = int(cell)
        if int(cell) > maxVal:
            maxVal = int(cell)
    checksum += (maxVal - minVal)
    
    #print maxVal, minVal

print checksum

#print puzInput
