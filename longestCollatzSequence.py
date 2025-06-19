#Longest Collatz Sequence


def collatz_length(n, lengthDict):
    original = n
    count = 0
    sequence = []

    while n not in lengthDict:
        sequence.append(n)
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        count += 1
    total_length = count + lengthDict[n]

    for val in sequence:
        lengthDict[val] = total_length
        total_length -= 1
    
    return lengthDict[original]


    

# 3 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2
# seqList {1:1, 2:2}
# Use memoization in this problem by using a hashmap to track values we already know so we don't do extra work
collatz_lengths = {1:1}

max_len = 0
max_num = 1
for i in range(1, 1000000):
    length = collatz_length(i, collatz_lengths)
    if length > max_len:
        max_len = length
        max_num = i
print(max_num)
