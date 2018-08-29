# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    n = len(A)
    
    # at least 3 elements to have peak(s)
    if n < 3:
        return 0
        
    # prefix sum to peaks count
    peaks = [0]*n
    for index in range(2,n):
        if A[index-1] > A[index-2] and A[index-1] > A[index]:
            peaks[index-1] += 1
        peaks[index] = peaks[index-1]
        
    # case no peaks
    if peaks[n-1] == 0:
        return 0
        
    # initialize divisor
    maxDivisor = 1
    
    for arrayDivisor in range(1, n):
        if n % arrayDivisor == 0:
            blockLength = n//arrayDivisor
            index = 0
            
            # detect if peaks are present in each block
            while index <= n - blockLength:
                if peaks[index+blockLength-1] - peaks[index-1 if index != 0 else index] == 0:
                    break
                index += blockLength
            
            if index == n:
                maxDivisor = max(maxDivisor, arrayDivisor)
        arrayDivisor += 1
    return maxDivisor