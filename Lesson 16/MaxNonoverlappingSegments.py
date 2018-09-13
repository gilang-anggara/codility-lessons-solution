# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, B):
    # write your code in Python 3.6
    n = len(A)
    if n == 0:
        return 0
        
    low = A[0]
    high = B[0]
    count = 1
    for i in range(1, n):
        if A[i] > high:
            high = B[i]
            count += 1
        
    return count