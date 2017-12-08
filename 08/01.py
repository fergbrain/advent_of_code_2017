import re

with open("input") as f:
    puzInput = f.readlines()

'''
puzInput = [    "b inc 5 if a > 1",
                "a inc 1 if b < 5",
                "c dec -10 if a >= 1",
                "c inc -20 if c == 10"]
'''

register = {}


def inc_dec(reg, act, val):
    if reg not in register:
        register[reg] = 0
    if act == "inc":
        register[reg] += int(val)
    elif act == "dec":
        register[reg] -= int(val)
    else:
        print "Error: %s" % act
        exit()

for inst in puzInput:
    result = re.match("^([a-z]+) (inc|dec) (-?[\d]+) if ([a-z]+) (.*) (-?[\d]+)", inst)
    if result.group(4) not in register:
        register[result.group(4)] = 0
    if result.group(5) == "==":
        if register[result.group(4)] == int(result.group(6)):
            inc_dec(result.group(1), result.group(2), result.group(3))
    elif result.group(5) == "!=":
        if register[result.group(4)] != int(result.group(6)):
            inc_dec(result.group(1), result.group(2), result.group(3))
    elif result.group(5) == "<":
        if register[result.group(4)] < int(result.group(6)):
            inc_dec(result.group(1), result.group(2), result.group(3))
    elif result.group(5) == "<=":
        if register[result.group(4)] <= int(result.group(6)):
            inc_dec(result.group(1), result.group(2), result.group(3))
    elif result.group(5) == ">":
        if register[result.group(4)] > int(result.group(6)):
            inc_dec(result.group(1), result.group(2), result.group(3))
    elif result.group(5) == ">=":
        if register[result.group(4)] >= int(result.group(6)):
            inc_dec(result.group(1), result.group(2), result.group(3))

print register[max(register, key=register.get)]