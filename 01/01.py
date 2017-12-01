with open('input', 'r') as f:
    puzInput = f.read().replace('\n', '')

captcha = 0

if int(puzInput[0]) == int(puzInput[len(puzInput)-1]):
    captcha += int(puzInput[0])

for i in range(1, len(puzInput)):
    if int(puzInput[i]) == int(puzInput[i-1]):
        print str(i) + ": " + puzInput[i-1] + " | " + puzInput[i]
        captcha += int(puzInput[i])

print captcha
