# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S, P, Q):
    # write your code in Python 3.6
    A = [0]*len(S)
    APrefixSum = [0]*len(S)
    
    C = [0]*len(S)
    CPrefixSum = [0]*len(S)
    
    G = [0]*len(S)
    GPrefixSum = [0]*len(S)
    
    T = [0]*len(S)
    TPrefixSum = [0]*len(S)
    
    # map all the character
    for index in range(len(S)):
        if S[index] == 'A':
            A[index] = 1
        elif S[index] == 'C':
            C[index] = 1
        elif S[index] == 'G':
            G[index] = 1
        else:
            T[index] = 1
    
    #prefix sum
    sumTemp = 0
    for index in range(len(S)):
        sumTemp += A[index]
        APrefixSum[index] = sumTemp
        
    sumTemp = 0
    for index in range(len(S)):
        sumTemp += C[index]
        CPrefixSum[index] = sumTemp
        
    sumTemp = 0
    for index in range(len(S)):
        sumTemp += G[index]
        GPrefixSum[index] = sumTemp
        
    sumTemp = 0
    for index in range(len(S)):
        sumTemp += T[index]
        TPrefixSum[index] = sumTemp
        
    # Get changes
    result = [0]*len(P)
    for index in range(len(P)):
        if APrefixSum[Q[index]] - APrefixSum[P[index]] > 0 or A[P[index]] == 1:
            result[index] = 1 
        elif CPrefixSum[Q[index]] - CPrefixSum[P[index]] > 0 or C[P[index]] == 1:
            result[index] = 2
        elif GPrefixSum[Q[index]]- GPrefixSum[P[index]] > 0 or G[P[index]] == 1:
            result[index] = 3
        else:
            result[index] = 4
    
    return result