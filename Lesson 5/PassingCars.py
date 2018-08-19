# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    # A != [], length N
    # consecutive elmnt
    # A only 0s and 1s
    
    N = len(A)
    eSum = 0
    pSum = [0]*N
    
    for index in range(N):
        eSum += A[index]
        pSum[index] = eSum
    
    count = 0
    index = 0
    for element in A:
        if element == A[0]:
            count += pSum[-1] - pSum[index]
            
        index += 1
        
    return count