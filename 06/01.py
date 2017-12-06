import csv

puzInput = list(csv.reader(open('input', 'rb'), delimiter='\t'))

puzInput = puzInput[0]
for i in range(0, len(puzInput)):
    puzInput[i] = int(puzInput[i])


memoryState = []

# puzInput = [0, 2, 7, 0]

print puzInput

memoryState.append(puzInput)
# print memoryState

def mem_realloc(mem_bank):
    bank_offset = mem_bank.index(max(mem_bank))
    temp_bank = max(mem_bank)
    mem_bank[bank_offset] = 0

    # print mem_bank

    ptr = 1
    while temp_bank > 0:
        # print (ptr + bank_offset ) % len(mem_bank)
        mem_bank[(ptr + bank_offset ) % len(mem_bank) ] += 1
        temp_bank -= 1
        ptr += 1
        # print mem_bank

    return mem_bank

while True:
    newState = mem_realloc(puzInput[:])
    # print "New State: %s" % newState
    if newState in memoryState:
        break
    else:
        puzInput = newState
        memoryState.append(newState[:])

# print memoryState
print "State: %s" % newState
print "Total Cycles: %s" % len(memoryState)
print "Diff Cycle: %s" % (len(memoryState) - memoryState.index(newState))