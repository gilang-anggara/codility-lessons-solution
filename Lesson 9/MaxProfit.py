# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    minimumPrice = 200001
    maxProfit = 0
    
    for element in A:
        minimumPrice = min(minimumPrice, element)
        maxProfit = max(maxProfit, element - minimumPrice)
        
    return maxProfit