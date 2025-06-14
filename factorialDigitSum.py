## Factorial Digit Sum

def sumOfDigits(num):
    factorial = getFactorial(num)
    print(factorial)
    num = factorial
    sum = 0
    while num >= 10:
        lastDigit = num % 10
        sum += lastDigit
        num //= 10

    print('Ans: ', sum+num)
    return sum+num



def getFactorial(num):
    factorial = 1
    for i in range(1, num+1):
        factorial *= i

    return factorial

sumOfDigits(100)