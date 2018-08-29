# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    n = len(A)
    size = 0
    index = -1
    
    for i in range(n):
        if size == 0:
            size += 1
            value = A[i]
            candidateIndex = i
        else:
            if value != A[i]:
                size -= 1
            else:
                size += 1
                
    candidate = -1
    if size > 0:
        candidate = value
    
    count = 0
    
    if candidate:
        for element in A:
            if element == candidate:
                count += 1
    
    if count > n//2:
        index = candidateIndex
    
    return index