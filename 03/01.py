import math

puzInput = 368078


def ulam_spiral(n):
    return int(4*math.pow(int(n), 2)-3*int(n)+1)

def inv_ulam_spiral(f):
    return  (1.0/8.0) * (3.0 + math.sqrt(16.0*float(f)-7.0)), (1.0/8.0) * (3.0 - math.sqrt(16.0*float(f)-7.0))

def manhat_distance(a, b):

    b_ring = int(math.floor(inv_ulam_spiral(float(b))[0]))
    b_offset = ulam_spiral(b_ring)
    b_offset_1 = ulam_spiral(b_ring+1)
    b_quarter_distance = (b_offset_1-b_offset-1)/4
    b_closet_quarter_distance = abs(b_offset - b)
    for i in range(b_offset + b_quarter_distance, b_offset_1, b_quarter_distance):
        if abs(i - b) < b_closet_quarter_distance:
            b_closet_quarter_distance = abs(i - b)
    return b_ring + b_closet_quarter_distance



print manhat_distance(1, 12)
print manhat_distance(1, 23)
print manhat_distance(1, 1024)
print manhat_distance(1, 368078)