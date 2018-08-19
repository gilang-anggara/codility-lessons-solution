# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    myDict = {}
    
    for element in A:
        if element not in myDict:
            myDict[element] = 1
    
    return len(myDict)