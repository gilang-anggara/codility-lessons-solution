# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(K, M, A):
    # write your code in Python 3.6
    N = len(A)
    minSum = max(A)
    maxSum = sum(A)
    
    if K == 1:
        return maxSum
    
    if K == N:
        return minSum
        
    while minSum <= maxSum:
        largeSum = (minSum + maxSum) // 2
        
        tempSum = 0
        count = 1
        
        for element in A:
            tempSum += element
            
            if tempSum > largeSum:
                tempSum = element
                count += 1
                if count > K:
                    break
        
        if count <= K:
            maxSum = largeSum - 1
            result = largeSum
        else:
            minSum = largeSum + 1
    
    return result