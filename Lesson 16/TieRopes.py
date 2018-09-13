# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(K, A):
    # write your code in Python 3.6
    n = len(A)
    
    count = 0
    tempLength = 0
    for element in A:
        tempLength += element
        if tempLength >= K:
            count += 1
            tempLength = 0
        
    return count