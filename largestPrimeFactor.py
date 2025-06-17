# Largest Prime Factor

import math

#Method to see if a number is prime
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

def largestPrimeFactor(num):
    
    factors = set()
    for i in range(2, math.floor(math.sqrt(num)+1)):
        if(num % i == 0):
            factors.add(i)
            factors.add(num/i)

# we use max to get the max number in the possible factors. we check if that is prime and if it is we return that number. If not we remove the number and go to next max.
    while True:
        maxNum = max(factors)
        if(isPrime(maxNum)):
            return maxNum
        else:
            factors.remove(maxNum)





print(largestPrimeFactor(13195))
print(largestPrimeFactor(600851475143))