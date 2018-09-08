# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    n = len(A)
    
    if n == 0:
        return []
        
    maxElement = max(A)
    
    # space O(N) as maxElement <= 2*N
    x = [0] * (maxElement + 1)
    
    
    myDict = {}
    
    # time O(N) space O(N)
    for element in A:
        if element in myDict:
            myDict[element] += 1
        else:
            myDict[element] = 1
    
    # time O(N log N)
    for p, q in myDict.items():
        k = p
        while k <= maxElement:
            x[k] += q
            k += p
    
    return [n - x[k] for k in A]
    
    
        
        