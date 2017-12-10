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
    
    l_temp = l + l
    l_sel = l_temp[p:(p+i)]
    l_sel.reverse()
    
    for j in range(i):
        l[(p+j)%ln] = l_sel[j]
    p = (p + i + s) % ln
    s += 1

#print puzInput
print l[0] * l[1]