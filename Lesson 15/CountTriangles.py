# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    n = len(A)
    result = 0
    
    A.sort()
    
    for p in range(n-2):
        r = p + 2
        
        for q in range(p + 1, n - 1):
            while r < n and A[p] + A[q] > A[r]:
                r += 1
            result += r - q - 1
    
    return result