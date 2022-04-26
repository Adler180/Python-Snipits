import math

def toBinary(x):
    binar = []
    num = x
    while num > 0:
        binar.append(num%2)
        num = math.floor(num/2)
    ret = []
    for i in range(1, len(binar)+1): ret.append(binar[len(binar)-i])
    return ret
