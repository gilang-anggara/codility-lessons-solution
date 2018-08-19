# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N, A):
    # write your code in Python 3.6
    
    counters = [0]*N
    currentMax = 0
    maxCounterValue = 0
    
    for element in A:
        position = element - 1
        if element <= N:
            counters[position] = counters[position]+1 if counters[position] > maxCounterValue else maxCounterValue+1
            currentMax = max(counters[position], currentMax)
        else:
            maxCounterValue = currentMax
    
    for index in range(N):
        if counters[index] < maxCounterValue:
            counters[index] = maxCounterValue
    
    return counters
