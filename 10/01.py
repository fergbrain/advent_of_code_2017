import csv

puzInput = list(csv.reader(open('input', 'rb'), delimiter=','))
#puzInput = [3, 4, 1, 5]
puzInput = puzInput[0]

for a in range(0,len(puzInput)):
    puzInput[a] = int(puzInput[a])
    

ln = 256 #255
l = list(range(ln))
p = 0
s = 0

for i in puzInput:
    if ( p % len(l) ) >= ( (p+i+1) % len(l) ):
        temp_list = l[p % len(l):] + l[:(p+i) % len(l)] 
        temp_list = temp_list[::-1]
        
        k = 0
        for j in range( (p) % len(l), len(l)):
            l[j] = temp_list[k]
            k += 1
        for j in range(0, len(temp_list) - k  ):
            l[j] = temp_list[k]
            k += 1
    else:
        temp_list = l[p % len(l):(p+i) % len(l)]
        temp_list = temp_list[::-1]
        k = 0
        for j in range(p % len(l), (p+i) % len(l)):
            l[j] = temp_list[k]
            k += 1
    p += i + s
    s += 1

#print puzInput
print l[0] * l[1]