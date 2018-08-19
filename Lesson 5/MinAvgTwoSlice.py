# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    prefSum = [0]*(len(A)+1)
    sumTemp = 0
    for index in range(len(A)):
        sumTemp += A[index]
        prefSum[index+1] = sumTemp
        
    minIndex = 0
    minAvg = prefSum[len(A)]/len(A)
    for index in range(len(A)):
        avg = (prefSum[len(A)] - prefSum[index])/(len(A)-index)
        if avg < minAvg:
            minIndex = index
            minAvg = avg
    
    return minIndex
    