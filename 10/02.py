with open('input', 'r') as myfile:
    fileInput=myfile.read().replace('\n', '')
puzInput = []
for char in fileInput:
    puzInput.append(ord(char))

puzInput += [17, 31, 73, 47, 23]

#print "puzInput: %s" % puzInput
for a in range(0,len(puzInput)):
    puzInput[a] = int(puzInput[a])

ln = 256 #255
l = list(range(ln))
p = 0
s = 0

for _ in range(64):
    for i in puzInput:
    
        l_temp = l + l
        l_sel = l_temp[p:(p+i)]
        l_sel.reverse()
    
        for j in range(i):
            l[(p+j)%ln] = l_sel[j]
        p = (p + i + s) % ln
        s += 1

dh = []

for a in range(0,256,16):
    dx = l[a]
    for b in range(a+1,a+16):
        dx = dx ^ l[b]
    dh.append(dx)

cb = ''
for x in dh:
    cb += '{0:02x}'.format(x)

print cb

#not eb4387e39616c7b99e67fcc231d77467
#not e06c0ef7defab967a09e9fca28d3fbe4