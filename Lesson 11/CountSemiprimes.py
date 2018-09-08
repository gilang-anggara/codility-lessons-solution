# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N, P, Q):
    # write your code in Python 3.6
    
    x = [0] * (N + 1)
    
    x[0] = -1
    
    i = 2
    
    while i * i <= N:
        k = i * i
        while k <= N:
            if x[k] == 0:
                x[k] = i
            k += i
        i += 1
    
    M = len(P)
    
    pSum = 0
    detector = [0] * (N + 1)
    result = []
    
    for i in range(4, N + 1):
        if x[i] != 0 and x[i//x[i]] == 0:
            pSum += 1
        detector[i] = pSum
    
    for i in range(M):
        result.append(detector[Q[i]] - detector[P[i]-1])
        
    return result