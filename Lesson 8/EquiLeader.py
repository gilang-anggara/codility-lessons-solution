# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    n = len(A)
    size = 0
    
    for i in range(n):
        if size == 0:
            size += 1
            value = A[i]
        else:
            if value != A[i]:
                size -= 1
            else:
                size += 1

    if size < 1:
        return 0
    
    count = 0
    
    for element in A:
        if element == value:
            count += 1

    if count > n/2:
        leader = value
    else:
        return 0
    
    left = 0
    right = count
    equiLeader = 0
    for i in range(n):
        if A[i] == leader:
            left += 1
            right -= 1
        if left > (i + 1)//2 and right > (n - i - 1)//2:
            equiLeader += 1
            
    return equiLeader