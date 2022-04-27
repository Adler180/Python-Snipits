def gcd(r0, r1):
	#Returns the greatest common divisor of r0 and r1
    if r0 == 0:
        return r1
    else:
        if r1 == 0:
            return r0
        else:
            if (r0 % r1 == 0):
                return r1
            else:
                temp = r0 %r1
                return gcd(r1, temp)
