# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    n = len(A)
    
    A.sort()
    
    # all positive + 0
    if A[0] >= 0:
        return 2 * A[0]
        
    # all negative + 0
    if A[n - 1] <= 0:
        return -2 * A[n - 1]
        
    # initialize minimum sum, guaranteed positive
    minSum = 2 * A[n - 1]
    
    low = 0
    high = n - 1
    
    while low <= high:
        tempSum = abs(A[low] + A[high])
        
        minSum = min(tempSum, minSum)
        
        if abs(A[low + 1] + A[high]) <= tempSum:
            low += 1
        elif abs(A[low] + A[high - 1]) <= tempSum:
            high -= 1
        else:
            high -= 1
            low += 1
    
    return minSum
        
            