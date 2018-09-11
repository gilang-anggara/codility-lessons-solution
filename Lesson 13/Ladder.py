# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, B):
    L = len(A)
    P_MOD = (1 << max(B)) - 1 # 2 ** max(B) - 1
    sequenceSolution = []
    
    fiboSeq = [0] * (L + 2)
    fiboSeq[1] = 1
    for i in range(2, L + 2):
        fiboSeq[i] = (fiboSeq[i - 1] + fiboSeq[i - 2]) & P_MOD
    
    # iterate through list
    for i in range(L):
        N = A[i]
        MOD = (1 << B[i]) - 1
        
        sequenceSolution.append(fiboSeq[N + 1] & MOD)
        
    return sequenceSolution
    
    