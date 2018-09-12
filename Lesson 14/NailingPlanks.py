# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def isNailed(A, B, C, end):
    N = len(A)
    M = len(C)
    
    SC = [0] * (2 * M + 1)
    
    for i in range(end):
        SC[C[i]] = 1
    
    for i in range(1, 2 * M + 1):
        SC[i] += SC[i-1]
    
    for i in range(N):
        if not SC[B[i]] - SC[A[i]-1]:
            return False
    
    return True
    
def solution(A, B, C):
    M = len(C)
    
    low = 1
    high = M
    
    result = -1
    while low <= high:
        mid = (low + high) // 2
        
        if isNailed(A, B, C, mid):
            high = mid - 1
            result = mid
        else:
            low = mid + 1
        
    return result