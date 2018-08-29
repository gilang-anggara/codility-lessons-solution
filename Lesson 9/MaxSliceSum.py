# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    maxEnding = 0
    maxSlice = A[0]
    
    for element in A:
        maxEnding = max(element, maxEnding + element)
        maxSlice = max(maxSlice, maxEnding)
        
    return maxSlice