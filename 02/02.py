import csv

puzInput = list(csv.reader(open('input', 'rb'), delimiter='\t'))

checksum = 0

for row in puzInput:

    for dividend in row:
        for divisor in row:
            if ( int(dividend)%int(divisor) == 0 ) and ( int(dividend) != int(divisor) ):
                print "Found it: %d/%d = %d" %(int(dividend), int(divisor), int(dividend)/int(divisor))
                checksum += int(dividend)/int(divisor)
    #print row    
    #print maxVal, minVal

print checksum

#print puzInput
