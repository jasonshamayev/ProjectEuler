# Sum Square Difference

def sumSquares(x):
    sum = 0
    for i in range(1,x+1):
        sum += i**2
    return sum


def squareSum(x):
    # remember summation formulas sum of x = x(x+1)/2
    sum = x*(x+1)/2
    squared = sum**2
    return squared

difference = squareSum(100) - sumSquares(100)
print(difference)