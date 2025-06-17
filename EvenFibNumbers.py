#Even Fibonacci Numbers

def fibonacci_sequence_sum(upToNumber):
    # F(n) = F(n-2) + F(n-1)
    fn2 = 0
    fn1 = 1
    sum = 0
    while True:
        
        fn = fn2 + fn1
        if(fn > upToNumber):
            return sum
        if(fn % 2 == 0):
            sum += fn
        fn2 = fn1
        fn1 = fn




sum = fibonacci_sequence_sum(4000000)
print(sum)