import csv

puzInput = list(csv.reader(open('input', 'rb'), delimiter=','))

#puzInput = [3, 4, 1, 5]
puzInput = puzInput[0]

for a in range(0,len(puzInput)):
    puzInput[a] = int(puzInput[a])
    

cir_list_max = 255 #255

cir_list = []

current_pos = 0

skip = 0

for i in range(0, cir_list_max+1):
    cir_list.append(i)

print "Cicular List: %s" % cir_list

for i in puzInput:
    print "Length: %s" % i
    print "Current Pos: %s" % current_pos
    print "Skip: %s" % skip
    print "Getting [%s,%s]" % (current_pos % (len(cir_list) ),( (current_pos+i-1) % len(cir_list)))
    if ( current_pos % len(cir_list) ) >= ( (current_pos+i+1) % len(cir_list) ):
        print "Wrapping"
        temp_list = cir_list[current_pos % len(cir_list):] + cir_list[:(current_pos+i) % len(cir_list)] 
        print "Temp: %s" % temp_list
        temp_list = temp_list[::-1]
        print "Temp (rev): %s" % temp_list
        
        k = 0
        for j in range( (current_pos) % len(cir_list), len(cir_list)):
            print "Putting %s into position %s" % (temp_list[k], j)
            try:
                cir_list[j] = temp_list[k]
            except Exception as e:
                print "j: %s | k: %s" % (j,k)
                print e
                exit()
            k += 1
              
        for j in range(0, len(temp_list) - k  ):
            print "Putting %s into position %s" % (temp_list[k], j)
            try:
                cir_list[j] = temp_list[k]
            except Exception as e:
                print "j: %s | k: %s" % (j,k)
                print e
                exit()
            k += 1
        
        
    else:
        temp_list = cir_list[current_pos % len(cir_list):(current_pos+i) % len(cir_list)]
        print "Temp: %s" % temp_list
        temp_list = temp_list[::-1]
        #temp_list = cir_list[(current_pos+i-1) % len(cir_list) : (current_pos-1) % len(cir_list):-1]
        print "Temp (rev): %s" % temp_list
        k = 0
        for j in range(current_pos % len(cir_list), (current_pos+i) % len(cir_list)):
            print "Putting %s into position %s" % (temp_list[k], j)
            try:
                cir_list[j] = temp_list[k]
            except Exception as e:
                print "j: %s | k: %s" % (j,k)
                print e
                exit()
            k += 1
    

        
        
        
    print "Cicular List: %s" % cir_list
    current_pos += i + skip
    skip += 1
    print ""

#print puzInput
print cir_list[0] * cir_list[1]