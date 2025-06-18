#Highly Divisible Triangular Number
import math

# divisor count represents the number of divisors we want to return, in this case it will be 501.
def triangularNumber(divisorCount):
    i = 1
    num = 1
    while (True):
        
        print('triangle num:', num)
        count = getDivisors(num)
        i += 1
        num += i
        if(count > divisorCount):
            return count



# in this function we will figure out how many divisors a number has. We will return the count. 
def getDivisors(triangleNum):
    divisors = set()
    divisors.add(1)
    divisors.add(triangleNum)
    # The largest possible factor will be the square root, so we use that. We use the floor method to make sure if it's not a perfect square we get the greatest integer less than or equal to the value
    for i in range (2, math.floor(math.sqrt(triangleNum) + 1)):
        if(i**2 == triangleNum):
            divisors.add(i)
        elif (triangleNum % i == 0):
            divisors.add(i)
            divisors.add(triangleNum/i)
    
    #print('DIVISORS', divisors)
    print('divisor COUNT:', len(divisors))

    return len(divisors)


triangularNumber(500)