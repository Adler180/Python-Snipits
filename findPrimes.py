import math

def find_prime(n):
	#Finds the Primes the number n is divisible by and returns them. If n is Prime it returns "Is prime number"
    for i in range(2, n):
        if math.floor(n/i) == n/i:
            return i
    return "Is prime number"
