# Pandigital Prime

import math
from itertools import permutations

def isPrime(num):
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range (2, math.floor(math.sqrt(num) + 1)):
        if(num % i == 0):
            return False
    return True
    
# needs every digit 123,456,789 so at least 9 digits to start

def nDigitPandigital():
    for n in range(9, 0, -1):
        digits = ''.join(str(i) for i in range(1,n+1))
        for p in sorted(permutations(digits), reverse=True):
            num = int(''.join(p))
            if isPrime(num):
                return num
    return 0



ans = nDigitPandigital()
print(ans)