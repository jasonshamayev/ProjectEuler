#Summation of Primes

import math

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
    
def sumOfPrimes(maxNum):
    sum = 0
    for i in range (2, maxNum+1):
        if(isPrime(i)):
            sum += i


    return sum



sum = sumOfPrimes(2000000)
print(sum)
