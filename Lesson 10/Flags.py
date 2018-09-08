# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    n = len(A)
    
    if n < 3:
        return 0
    
    peakIndex = []
    for i in range(1, n-1):
        if A[i] > A[i-1] and A[i] > A[i+1]:
            peakIndex.append(i)
            
    numberOfFlags = len(peakIndex)
    
    if numberOfFlags == 0:
        return 0
        
    flagMaxDistance = peakIndex[-1] - peakIndex[0]
    maxFlag = 0
    
    possible = 1
    for i in range(numberOfFlags, 0, -1):
        if flagMaxDistance//i + 1 >= i:
            possible = i
            break

    i = 1
    while i <= possible:
        comparable = peakIndex[0]
        count = 1
        for element in peakIndex:
            if element - comparable >= i:
                comparable = element
                count += 1
                if count == i:
                    break
        if count == i:
            maxFlag = i
            
        i += 1
    
    return maxFlag