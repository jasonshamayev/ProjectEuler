# 10 000st Prime

import math

def getXthPrime(num):
    count = 0
    i = 2
    while(count < num):
        if(isPrime(i)):
            count += 1
        i += 1
    
    return i-1

def isPrime(num):
    divisors = set()
    for i in range (1, math.floor(math.sqrt(num) + 1)):
        if(i**2 == num):
            return False

        if(num % i == 0):
            divisors.add(i)
            divisors.add(num/i)
    if(len(divisors) == 2):
        return True
    else:
        return False

print(getXthPrime(10001))