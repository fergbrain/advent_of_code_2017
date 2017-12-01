with open('input', 'r') as f:
    puzInput = f.read().replace('\n', '')

captcha = 0

for i in range(0, len(puzInput)):
    if i >= len(puzInput)/2:
        j = i - len(puzInput)/2
    else:
        j = i + len(puzInput)/2
    if int(puzInput[i]) == int(puzInput[j]):
        print str(i) + ": " + puzInput[i] + " | " + str(j) + ": " + puzInput[j]
        captcha += int(puzInput[i])

print captcha
