puzInput = []

with open('input') as f:
    for line in f:
        puzInput.append(int(line))

#puzInput = [0,3,0,1,-3]

ptr = 0


def jmp(stack, ptr):
    ptr_old = ptr
    ptr_value = stack[ptr_old]
    stack[ptr_old] += 1
    ptr = ptr_old + ptr_value
    # print stack, ptr
    return stack, ptr

i = 1
puzInput, cur_pos = jmp(puzInput, 0)
while True:
    try:
        puzInput, cur_pos = jmp(puzInput, cur_pos)
        i += 1
    except IndexError:
        print i
        break