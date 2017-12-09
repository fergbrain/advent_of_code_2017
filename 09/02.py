#puzInput = "{{{},{},{{}}}}" #16
#puzInput = "{<a>,<a>,<a>,<a>}" # 1
#puzInput = "{{<ab>},{<ab>},{<ab>},{<ab>}}" # 9
#puzInput = "{{<!!>},{<!!>},{<!!>},{<!!>}}" # 9
#puzInput = "{{<a!>},{<a!>},{<a!>},{<ab>}}" # 3

with open('input', 'r') as myfile:
    puzInput=myfile.read().replace('\n', '')

#puzInput = "{{{{{{{{<a}!!!aa!!!>ua,a,!>{!>!!!>a>,"
#puzInput = "{{{{{{{{,},}},{{},}}}}}}"
#puzInput = "{{{{{{{{}}},{{}}}}}}}" #49?

#puzInput = "{1{2{3{4{5{6{7{8}7}6},{6{7}6}5}4}3}2}1}" #49

group = {}
level = 0

garbageState = False;
ignoreState = False;
isSibling = False

garbageCount = 0

for char in puzInput:
    #print level
    if isSibling:
        if char != "{":
            isSibling = False
    #print "Processing: %s" % char
    if ignoreState:
        print "Ignoring: %s" % char
        ignoreState = False
        continue
    elif garbageState:
        print "Garbage State"
        if char == "!":
            ignoreState = True
        elif char == ">":
            print "Exiting garbage state"
            garbageState = False
        else:
            garbageCount += 1
        continue
    elif char == "{":
        if level == 0:
            group[0] = 1
            level += 2
        else:
            if isSibling:
                group[len(group)] = level
                isSibling = False
                level += 1
            else:
                group[len(group)] = level
                level += 1
    elif char == "}":
        level -= 1
        continue
    elif char == ",":
        isSibling = True
        continue
    elif char == "<":
        garbageState = True
        print "Entering Garbage State"
    else:
        print "Missing branch for: %s" % char
    #print "%s, %s, %s" % (ignoreState, garbageState, group)
    
group_sum = 0
for key, value in group.iteritems():
    group_sum += value
    
print group_sum # 428642 is too high, 11089 is correct
print garbageCount