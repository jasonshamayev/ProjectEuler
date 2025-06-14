## Multiples of 3 or 5
import math

def sum_of_multiples_3_or_5(num):
    ## arithmetic series sum = times it goes into num * (multiple (ex: 3 or 5) + last number in series before num)/2
    ## sum = an * (m+ ni)/2
    threeSum = sum_of_m(3,num-1)
    print(threeSum)
    fiveSum = sum_of_m(5,num-1)
    print(fiveSum)
    fiveteenSum = sum_of_m(15,num-1)
    print(fiveteenSum)
    sum = threeSum + fiveSum - fiveteenSum
    print('Ans: ', sum)
    return sum

#split the problem and get sum of 1 number
def sum_of_m(m, num):
    an = math.floor(num/m)
    print(an)
    ni = an*m
    sum = an * (m+ni)/2
    return sum

sum_of_multiples_3_or_5(1000)