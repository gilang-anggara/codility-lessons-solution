# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    n = len(A)
    
    left = [0]*n
    
    # max left slice
    for i in range(1, n-1):
        left[i] = max(0, left[i-1] + A[i])
    
    right = [0]*n
    
    # max right slice
    for i in range(n-2, 1, -1):
        right[i] = max(0, right[i+1] + A[i])
        
    
    # max sum
    doubleSlice = -10_000
    
    for i in range(1, n-1):
        doubleSlice = max(doubleSlice, left[i-1] + right[i+1])
    
    return doubleSlice
        