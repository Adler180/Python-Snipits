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


def eea(a, d, p):
    #Calculates a^d mod p
    variab = a
    x = toBinary(d)
    for i in range(1, len(x)):
        if x[i] == 1:
            variab = (variab * variab * a) % p
        if x[i] == 0:
            variab = (variab * variab) % p
    if variab != (a ** d) % p: return "An unknown error occurred" #Emergency check
    return variab
  
  
  def eeaSteps(a, d, p):
    #Calculates a^d mod p and prints out the Square and Multiplication Steps
    variab = a
    x = toBinary(d)
    for i in range(1, len(x)):
        if x[i] == 1:
            print(variab, "² *", a ,"mod", p, "=", (variab * variab * a) % p)
            variab = (variab * variab * a) % p
        if x[i] == 0:
            print(variab, "² mod ", p, "=", (variab * variab) % p)
            variab = (variab * variab) % p
    if variab != (a ** d) % p: return "An unknown error occurred" #Emergency check
    return variab
