# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    N = len(A)
    
    C = [-1]*N
    
    for index in range(N):
        if A[index] >= index:
            C[0] += 1
        else:
            C[index - A[index]] += 1
    
    # prefix sum
    t = 0
    for index in range(N):
        t += C[index]
        C[index] = t
    
    s = 0
    for index in range(N):
        s += A[index] if A[index] < N - index else N - index - 1
        
        if A[index] != N-1:
            s += C[index+A[index] if A[index] < N-index else N - 1]
        
        if s > 10000000:
            return -1
    
    return s